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
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')

    _sql_constraints = [
        ('unique_project_name', 'unique(name)', 'The project name must be unique.')
    ]

    def action_start_project(self):
        if self.state in ['draft', 'on_hold']:
            self.state = 'in_progress'

    def action_hold_project(self):
        if self.state in ['in_progress', 'completed', 'cancelled']:
            self.state = 'on_hold'

    def action_complete_project(self):
        if self.state in ['in_progress', 'on_hold']:
            self.state = 'completed'

    def action_cancel_project(self):
        if self.state != 'draft':
            self.state = 'cancelled'

    

    def unlink(self):
        rec = super().unlink()
        
        return rec