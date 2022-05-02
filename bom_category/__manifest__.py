# -*- coding: utf-8 -*-
{
    'name': "BOM category",

    'summary': """
       Route Category addon""",

    'description': """
        Adds two category fields to BOM model in MRP.
    """,

    'author': "Gonzalo Nuin",
    'website': "https://avanzosc.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'MRP',
    'version': '14.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bom_category_view.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
      
    ],
}
