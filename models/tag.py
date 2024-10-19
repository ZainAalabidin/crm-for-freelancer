from odoo import models, fields

class Tag(models.Model):
    _name = 'tag'
    _description = 'Tags For clients'

    name = fields.Char('Task Name', required=True)
    color = fields.Integer(string="Color Index")