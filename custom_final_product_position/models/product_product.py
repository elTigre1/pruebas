from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'
    _descriptiom = 'Product Product'

    quartering_location_ids = fields.One2many(comodel_name="quartering.location",
                                            inverse_name="product_id",
                                            string="Final Product")