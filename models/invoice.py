from odoo import models, fields

class Invoice(models.Model):
    _name = 'invoice'
    _description = 'Custom CRM for Invoice'

    payment_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], 'Payment Status')
    project_id = fields.Many2one('project', string='Project Name', required=True)
    client_id = fields.Many2one('client', string='Client Name', required=True)
    total_amount = fields.Float('Total Amount')
    due_date = fields.Date('Due Date')
