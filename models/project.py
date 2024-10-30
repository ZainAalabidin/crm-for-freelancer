from odoo import models, fields, api
from odoo.exceptions import UserError

class Project(models.Model):
    _name = 'project'
    _description = 'Project'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(default="New", readonly=1)
    name = fields.Char('Project Name', required=True, tracking="1")
    total_hours = fields.Float('Total Hours', compute="_compute_total_hours", store=True)
    client_id = fields.Many2one('client', string='Client Name', required=True, tracking="1")
    start_date = fields.Date('Start Date', tracking="1")
    end_date = fields.Date('End Date', tracking="1")
    task_ids = fields.One2many('task', 'project_id', string='Tasks', tracking="1")
    description = fields.Text('Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft', tracking="1")
    active = fields.Boolean(default=True)

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
            if any(task.is_done != True for task in self.task_ids):
                raise UserError('Cannot complete project with incomplete tasks')
            else:
                self.state = 'completed'

    def action_cancel_project(self):
        if self.state != 'draft':

            self.state = 'cancelled'

    @api.depends('task_ids.hours_spent', 'task_ids.is_done')
    def _compute_total_hours(self):
        for project in self:
            total_hours = sum(task.hours_spent for task in project.task_ids if task.is_done == True)
            project.total_hours = total_hours

    

    def unlink(self):
        rec = super().unlink()
        return rec


    @api.model
    def create(self, vals):
        res = super(Project, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('project_seq')
        return res
