from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'invoice'
    _description = 'Invoice for project'

    payment_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', string='Payment Status')
    project_id = fields.Many2one('project', string='Project Name', required=True, ondelete='cascade')
    client_id = fields.Many2one('client', string='Client Name', required=True, related='project_id.client_id')
    total_amount = fields.Float('Total Amount')
    due_date = fields.Date('Due Date')
    is_late = fields.Boolean('Is Late?')
    active = fields.Boolean(default=True)

    def check_due_date(self):
        records = self.search([])
        for record in records:
            if record.due_date and record.payment_status != 'paid' and record.due_date < fields.Date.today():
                record.is_late = True
            else:
                record.is_late = False