from datetime import timedelta
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _inherit = "project.task"
    task_reminder = fields.Boolean("Reminder")
    task_interval_duration = fields.Integer(
        string="Interval Time in days")
    project_task_reminder = fields.Boolean(
        related='project_id.project_task_reminder')

    @api.onchange('task_interval_duration', 'date_deadline')
    def _onchange_deadline_interval(self):
        if self.task_interval_duration > 0 and self.date_deadline:
            if self.date_deadline < fields.Date.today():
                raise UserError(
                    _('The deadline date has already passed.'))
            rem_date = self.date_deadline - timedelta(
                days=self.task_interval_duration)
            if rem_date < fields.Date.today():
                raise UserError(
                    _('The task reminder date has already passed.'))

    @api.model
    def _project_task_reminderby_email(self):
        task_rec = self.env['project.task'].search(
            [('date_deadline', '!=', None),
             ('user_id', '!=', None)])
        for rec in task_rec:
            self.due_day = due_day = (rec.date_deadline -
                                      fields.Date.today()).days
            if rec.project_id.project_task_reminder:
                interval = rec.project_id.project_interval_duration
            else:
                if rec.task_reminder:
                    interval = rec.task_interval_duration
                else:
                    interval = 0
            if interval > 0:
                if due_day == interval:
                    template_id = \
                        self.env['ir.model.data'].get_object_reference(
                            'task_due_date_indication',
                            'email_template_project_task_due_indication')[1]
                    if template_id:
                        email_template_rec = self.env['mail.template'].browse(
                            template_id)
                        vals = email_template_rec.generate_email(
                            rec.id, fields=None)
                        mail_id = self.env['mail.mail'].create(vals)
                        if mail_id:
                            mail_id._send()
