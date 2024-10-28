from odoo import models, fields, api
from odoo.exceptions import UserError

class Task(models.Model):
    _name = 'task'
    _description = 'Task Project.'

    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    is_done = fields.Boolean('Is Done?')
    project_id = fields.Many2one('project', string='Project Name', ondelete='cascade')
    hours_spent = fields.Float('Hours Spent')
    project_state = fields.Selection(related='project_id.state')

    # @api.model
    # def write(self, vals):
    #     if 'project_id' in vals:
    #         project = self.env[project].browse(vals['project_id'])
    #     else:
    #         project = self.project_id
        
    #     if project.state != 'in_progress':
    #         raise UserError("You cannot modify tasks when the related project is not in progress.")
    #     return super(Task, self).write(vals)
