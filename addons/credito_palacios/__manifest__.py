# -*- coding: utf-8 -*-
{
    'name': "credito_palacios",

    'summary': """
        Modulo orientado a la gestion de credito""",

    'description': """
        Sistema de Gestion Crediticia 
    """,

    'author': "Credito Palacio del Hogar",
    'website': "http://www.creditopalaciodelhogar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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

	'application':True
	'auto_installable':True
}
