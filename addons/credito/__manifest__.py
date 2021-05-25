# -*- coding: utf-8 -*-
{
    'name': "credito",

    'summary': """
        MOdulo de Credito - Encargado del proceso de revision y aprobacion Crediticia""",

    'description': """
        Se encargara de la operatividad de credito , dentro del proceso de ventas.
    """,

    'author': "	Credito Palacio del Hogar",
    'website': "http://www.palaciodelhogar.com",

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
   'application ': True
   'autoinstallable': True
}
