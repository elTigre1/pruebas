from odoo import models, fields

class QuarteringLocation(models.Model):
    _name = 'quartering.location'
    _description = 'Quartering Locations'
    _order = 'product_final_id,position'   

    
    product_final_id = fields.Many2one(comodel_name="product.final", string="Final Product")
    product_id = fields.Many2one(comodel_name="product.product")
    position = fields.Char(string="Position")