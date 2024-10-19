from odoo import models, fields

class Client(models.Model):
    _name = 'client'
    _description = 'Custom CRM for Client'

    name = fields.Char('Client Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    company = fields.Char('Company')
    social_media = fields.Text('Social Media Links')
    tag_ids = fields.Many2many('tag', string='Tags')
    interaction_history = fields.One2many('client.interaction', 'client_id', 'Interaction_History')