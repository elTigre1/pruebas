from odoo import models, fields


class ProductFinal(models.Model):
    _name = 'product.final'
    _description = 'Final Product'
   #_rec_name = 'display_name'

    #display_name = fields.Char(string="Name", compute="get_name")
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    # result_ids = fields.One2many(comodel_name="quartering.ubication",
    #                                     inverse_name="product_final_id")


    # def get_name(self):
    #     for rec in self:
    #         rec.display_name = str('['+ rec.code + ']' + ' ' + rec.name)
            

class QuarteringUbication(models.Model):
    _name = 'quartering.ubication'
    _description = 'Quartering Ubications'
    

    
    product_final_id = fields.Many2one(comodel_name="product.product", string="Final Product")
    product_id = fields.Many2one(comodel_name="quartering.ubication")
    position = fields.Char(string="Position")                        


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _descriptiom = 'Product Product'

    quartering_ubication_ids = fields.One2many(comodel_name="quartering.ubication",
                                            inverse_name="product_id",
                                            string="Final Product")
    
    
    