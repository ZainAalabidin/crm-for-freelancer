from odoo import models, fields

class Interaction(models.Model):
    _name = 'client.interaction'
    _description = 'Interaction Notes For clients'

    client_id = fields.Many2one('client', string='Client', required=True)
    date = fields.Datetime(string='Date')
    notes = fields.Text(string='Interaction Notes')