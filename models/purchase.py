from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _description = 'Purchase Order'

    order_date = fields.Date(string='Order Date', required=True)
    supplier = fields.Many2one('res.partner', string='Supplier', required=True)
    total_amount = fields.Float(string='Total Amount', required=True)
