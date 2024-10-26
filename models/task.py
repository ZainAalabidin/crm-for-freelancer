from odoo import models, fields

class Task(models.Model):
    _name = 'task'
    _description = 'Custom CRM for Task'

    name = fields.Char('Task Name', required=True)
    is_done = fields.Boolean('Is Done?')
    project_id = fields.Many2one('project', string='Project Name', ondelete='cascade')
    hours_spent = fields.Float('Hours Spent')
