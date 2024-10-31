from odoo import models, fields, api
from odoo.exceptions import UserError

class Task(models.Model):
    """
    Represents an individual task within a project, tracking details such as
    task name, description, completion status, time spent, and associated project.
    """
    _name = 'task'
    _description = 'Task Project.'

    name = fields.Char(
        'Task Name',
        required=True,
        help="The name of the task."
        )
    description = fields.Text(
        'Description',
        help="A description of the task's details and requirements."
        )
    is_done = fields.Boolean(
        'Is Done?',
        help="Indicates whether the task is completed."
        )
    project_id = fields.Many2one(
        'project',
        string='Project Name',
        ondelete='cascade',
        help="he project to which this task is linked. Deleting the project will delete the task."
        )
    hours_spent = fields.Float(
        'Hours Spent',
        help="The total hours spent on completing this task."
        )
    project_state = fields.Selection(
        related='project_id.state',
        help="Displays the current state of the project associated with this task."
        )