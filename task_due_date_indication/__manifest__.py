# -*- coding: utf-8 -*-
{
    'name': "Task Due Date Indication",
    'summary': """
        Track employee Task onetime and notify by Email them 
        before the task deadline. Easy to setup reminder days.
        App will send task Due Indication to employee and Manager by mail based 
        on the days set on Interval.""",
    'description': """
        -Send Task due date Indication to the Employee and Manager  by mail.
        -Easy to configure days when one wants to send task due date 
        indication email.
    """,
    'author': "Aktiv Software",
    'website': "www.aktivsoftware.com",
    'category': 'Project',
    'version': '13.0.1.0.0',
    'depends': ['project'],
    'data': [
        'data/deadline_reminder_cron.xml',
        'data/email_template_project_task_due_indication.xml',
        'views/project_project_views.xml',
        'views/project_task_views.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ]
}
