from odoo import models, fields, api

class StockItem(models.Model):
    _name = 'stock.item'
    _description = 'Stock Item'

    item_name = fields.Char(string='Item Name', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    location = fields.Char(string='Location', required=True)
