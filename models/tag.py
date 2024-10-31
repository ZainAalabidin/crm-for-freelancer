from odoo import models, fields

class Tag(models.Model):
    """
    This model represents a tag that can be assigned to clients for categorization
    and filtering purposes. Each tag has a unique name and an associated color.
    """
    _name = 'tag'
    _description = 'Tag For clients'

    name = fields.Char(
        'Task Name',
        required=True,
        help="The name of the tag, used to categorize clients."
        )
    color = fields.Integer(
        string="Color Index",
        help="Index representing the color of the tag in the Odoo color palette."
        )