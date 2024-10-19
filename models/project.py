from odoo import models, fields

class Project(models.Model):
    _name = 'project'
    _description = 'Custom CRM for Project'

    name = fields.Char('Project Name', required=True)
    total_hours = fields.Float('Total Hours')
    client_id = fields.Many2one('client', string='Client Name')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    task_ids = fields.One2many('task', 'project_id', string='Tasks')
    description = fields.Text('Description')