# -*- coding: utf-8 -*-

from odoo import models, fields


class MrpBom(models.Model):
    _inherit = 'mrp.bom'
    _description = 'Mrp Bom'

    category_id = fields.Many2one(comodel_name='bom.category')
    alt_category_id = fields.Many2one(comodel_name='alt.bom.category')
        

class BomCategory(models.Model):
    _name = 'bom.category'
    _description = 'Bom Category'

    name = fields.Char(string="Category:")
    bom_ids = fields.One2many(comodel_name="mrp.bom",
                           inverse_name="category_id",
                           string="BOMS using this category:")
    
class AltBomCategory(models.Model):
    _name = 'alt.bom.category'
    _description = 'Alt Bom Category'

    name = fields.Char(string="Category:")
    bom_ids = fields.One2many(comodel_name="mrp.bom",
                           inverse_name="alt_category_id",
                           string="BOMS using this category:")




    
 
