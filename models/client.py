from odoo import models, fields
from odoo.exceptions import UserError

class Client(models.Model):
    """
    This model represents a client in the CRM system, storing details
    such as contact information, company, social media links, tags,
    and interaction history. The model is designed to facilitate 
    communication tracking and follow-up management.
    """
    _name = 'client'
    _description = 'Client'

    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        'Client Name',
        required=True, 
        tracking="1",
        help="the The name of client."
        )
    email = fields.Char(
        'Email',
        tracking="1",
        help="Client's email address"
        )
    phone = fields.Char(
        'Phone',
        tracking="1",
        help="Client's phone number"
        )
    company = fields.Char(
        'Company',
        help="The company that client's associate with"
        )
    social_media = fields.Text(
        'Social Media Links',
        help="Links to the client's social media profiles."
        )
    tag_ids = fields.Many2many(
        'tag',
        string='Tags',
        tracking="1",
        help="Tags used to categorize clients."
        )
    interaction_history = fields.One2many(
        'client.interaction',
        'client_id',
        'Interaction_History',
        help="Records of all interactions with the client."
        )

    def send_followup_email(self):
        """
        Sends a follow-up email to the client using a predefined email template.
        
        Raises:
            UserError: If the email template is not found, an error is raised.
        """
        template_id = self.env.ref('custom_crm.email_template_followup').id
        if not template_id:
            raise UserError("Email template not found!")
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)