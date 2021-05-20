# -*- coding: utf-8 -*-
{
    'name': 'credito_modulo',

    'summary': 'Este modulo permite revisar el estado y datos de un cliente',

    'description': '  Este modulo permite revisar el estado y datos de un cliente.',

    'author': "Creditos Palacios del Hogar",
    'website': "http://www.palaciodelhogar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'application': True,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

