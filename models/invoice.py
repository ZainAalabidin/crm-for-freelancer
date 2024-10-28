from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'invoice'
    _description = 'Custom CRM for Invoice'

    payment_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', string='Payment Status')
    project_id = fields.Many2one('project', string='Project Name', required=True, ondelete='cascade')
    client_id = fields.Many2one('client', string='Client Name', required=True, related='project_id.client_id')
    total_amount = fields.Float('Total Amount')
    due_date = fields.Date('Due Date')

    # @api.onchange('project_id')
    # def _onchange_project_id(self):
    #     if self.project_id:
    #         self.client_id = self.project_id.client_id