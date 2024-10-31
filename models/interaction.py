from odoo import models, fields

class Interaction(models.Model):
    """
    This model represents individual interaction records for a client in the CRM.
    Each interaction includes details such as the associated client, the date
    of the interaction, and any relevant notes.
    """
    _name = 'client.interaction'
    _description = 'Interaction Notes For client'

    client_id = fields.Many2one(
        'client',
        string='Client',
        required=True,
        help="The client associated with this interaction."
        )
    date = fields.Datetime(
        string='Date',
        help="Date and time of the interaction."
        )
    notes = fields.Text(
        string='Interaction Notes',
        help="Notes or summary of the interaction with the client."
        )