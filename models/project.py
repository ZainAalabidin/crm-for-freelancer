from odoo import models, fields, api
from odoo.exceptions import UserError

class Project(models.Model):
    """
    This model represents a project in the system. It includes details like 
    project name, client, start and end dates, tasks associated with the project, 
    and the current project status. It also tracks total hours spent on the project.
    """
    _name = 'project'
    _description = 'Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(
        default='New',
        readonly=True,
        help="Unique reference for the project, auto-generated on creation."
        )
    name = fields.Char(
        'Project Name',
        required=True,
        tracking="1",
        help="The name of the project."
        )
    total_hours = fields.Float(
        'Total Hours',
        compute="_compute_total_hours",
        store=True,
        help="Total hours spent on the project, calculated from associated tasks."
        )
    client_id = fields.Many2one(
        'client',
        string='Client Name',
        required=True,
        tracking="1",
        help="The client associated with this project."
        )
    start_date = fields.Date(
        'Start Date',
        tracking="1",
        help="The start date of the project."
        )
    end_date = fields.Date(
        'End Date',
        tracking="1",
        help="The end date of the project."
        )
    task_ids = fields.One2many(
        'task',
        'project_id',
        string='Tasks',
        tracking="1",
        help="Tasks associated with this project."
        )
    description = fields.Text(
        'Description',
        help="A description of the project."
        )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ],
    string='State',
    default='draft',
    tracking="1",
    help="Current state of the project."
    )
    active = fields.Boolean(
        default=True,
        help="Indicates whether the project is active."
        )

    _sql_constraints = [
        ('unique_project_name', 'unique(name)', 'The project name must be unique.')
    ]

    def action_start_project(self):
        """
        Sets the project state to 'in_progress' if the current state is 'draft' or 'on_hold'.
        """
        if self.state in ['draft', 'on_hold']:
            self.state = 'in_progress'

    def action_hold_project(self):
        """
        Sets the project state to 'on_hold' if it is currently 'in_progress', 
        'completed', or 'cancelled'.
        """
        if self.state in ['in_progress', 'completed', 'cancelled']:
            self.state = 'on_hold'

    def action_complete_project(self):
        """
        Sets the project state to 'completed' if all tasks are completed and the 
        project is in progress or on hold. Raises a UserError if any tasks remain incomplete.
        
        Raises:
            UserError: If there are incomplete tasks when attempting to complete the project.
        """
        if self.state in ['in_progress', 'on_hold']:
            if any(task.is_done != True for task in self.task_ids):
                raise UserError('Cannot complete project with incomplete tasks')
            else:
                self.state = 'completed'

    def action_cancel_project(self):
        """
        Cancels the project, setting the state to 'cancelled' if it is not in 'draft' state.
        """
        if self.state != 'draft':

            self.state = 'cancelled'

    @api.depends('task_ids.hours_spent', 'task_ids.is_done')
    def _compute_total_hours(self):
        """
        Computes the total hours spent on the project by summing the hours of all 
        completed tasks.
        """
        for project in self:
            total_hours = sum(task.hours_spent for task in project.task_ids if task.is_done == True)
            project.total_hours = total_hours


    @api.model
    def create(self, vals):
        """
        Overrides the create method to generate a unique reference code for the 
        project using a sequence if the default reference is 'New'.
        
        Args:
            vals (dict): Dictionary of values used to create the new record.
            
        Returns:
            res (recordset): The newly created project record.
        """
        res = super(Project, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('project_seq')
        return res