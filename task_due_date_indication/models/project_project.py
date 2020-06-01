# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    project_task_reminder = fields.Boolean(string="Reminder")
    project_interval_duration = fields.Integer(string="Interval Time in days")

    @api.onchange('project_task_reminder')
    def _onchange_project_task_reminder(self):
        task_rec = self.env['project.task'].search(
            [('project_id', '=', self._origin.id)])
        if task_rec:
            if self.project_task_reminder:
                return {'warning': {
                    'title': ("Warning"),
                    'message': ('All the task of this project will get '
                                'reminder based on the interval set on this '
                                'project'),
                }}
