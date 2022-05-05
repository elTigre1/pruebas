# -*- coding: utf-8 -*-
{
    'name': "Custom Final Product Position",

    'summary': """
       Some new fields added for Final Product variants""",

    'description': """
       There have been some menus in slaes and stock added to customize final product codes and to add quartering locations. 
    """,

    'author': "Gonzalo Nuin",
    'website': "https://avanzosc.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '14.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','product','stock',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_final_view.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
      
    ],
}
