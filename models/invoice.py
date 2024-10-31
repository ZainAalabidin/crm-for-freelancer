from odoo import models, fields, api

class Invoice(models.Model):
    """
    This model represents an invoice for a project, tracking payment status,
    total amount, due dates, and whether the invoice is overdue. It also 
    automatically generates a unique reference for each invoice.
    """
    _name = 'invoice'
    _description = 'Invoice for project'

    ref = fields.Char(
        default='New',
        readonly=True,
        help="Unique reference for the invoice, auto-generated on creation."
        )
    payment_status = fields.Selection(
        [('paid', 'Paid'), ('unpaid', 'Unpaid')],
        default='unpaid',
        string='Payment Status',
        help="Indicates whether the invoice is paid or unpaid."
        )
    project_id = fields.Many2one(
        'project',
        string='Project Name',
        required=True,
        ondelete='cascade',
        help="The project associated with this invoice."
        )
    client_id = fields.Many2one(
        'client',
        string='Client Name',
        required=True,
        related='project_id.client_id',
        help="The client associated with the project."
        )
    total_amount = fields.Float(
        'Total Amount',
        help="The date by which payment for the invoice is due."
        )
    due_date = fields.Date(
        'Due Date',
        help="The date by which payment for the invoice is due."
        )
    is_late = fields.Boolean(
        'Is Late?',
        help="Indicates if the invoice is overdue and unpaid."
        )
    active = fields.Boolean(
        default=True,
        help="Indicates whether the invoice is active."
        )

    def check_due_date(self):
        """
        Checks if each unpaid invoice is past its due date. If an invoice is overdue, 
        it marks the 'is_late' field as True; otherwise, it is set to False.
        """
        records = self.search([])
        for record in records:
            if record.due_date and record.payment_status != 'paid' and record.due_date < fields.Date.today():
                record.is_late = True
            else:
                record.is_late = False

    @api.model
    def create(self, vals):
        """
        Overrides the create method to auto-generate a unique reference code for each 
        new invoice using a sequence if the default reference is 'New'.
        
        Args:
            vals (dict): The dictionary of values used to create the new record.
            
        Returns:
            res (recordset): The newly created invoice record.
        """
        res = super(Invoice, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('invoice_seq')
        return res