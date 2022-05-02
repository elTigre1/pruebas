from odoo import models, fields


class ProductFinal(models.Model):
    _name = 'product.final'
    _description = 'Final Product'
    _rec_name = 'display_name'

    display_name = fields.Char(string="Name", compute="get_name")
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code", required=True)
    result_ids = fields.One2many(comodel_name="product.template",
                                        inverse_name="product_final_id")


    def get_name(self):
        for rec in self:
            rec.display_name = str('['+ rec.code + ']' + ' ' + rec.name)
            

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Products'

    product_final_id = fields.Many2one(comodel_name="product.final", string="Final Product")
    position = fields.Integer(string="Position")


class CuttingUbicationProduct(models.Model):
    _name = 'cutting.ubication.product'
    _descriptiom = 'Cutting Ubication Products'

    name = fields.Char(string="Final Product", required=True)
    position = fields.Integer(string="Position")
    product = fields.Char(string="Final Product", required=True)