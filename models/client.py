from odoo import models, fields
from odoo.exceptions import UserError

class Client(models.Model):
    _name = 'client'
    _description = 'Client'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Client Name', required=True, tracking="1")
    email = fields.Char('Email', tracking="1")
    phone = fields.Char('Phone', tracking="1")
    company = fields.Char('Company')
    social_media = fields.Text('Social Media Links')
    tag_ids = fields.Many2many('tag', string='Tags', tracking="1")
    interaction_history = fields.One2many('client.interaction', 'client_id', 'Interaction_History')

    def send_followup_email(self):
        template_id = self.env.ref('custom_crm.email_template_followup').id
        if not template_id:
            raise UserError("Email template not found!")
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
