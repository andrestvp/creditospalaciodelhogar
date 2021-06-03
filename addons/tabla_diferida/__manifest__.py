# -*- coding: utf-8 -*-
{
    'name': "TablaDiferida",

    'summary': """
        Genera Tabla de Amortización para la venta""",

    'description': """
        Genera Tabla de Amortización
    """,

    'author': "Palacios del Hogar",
    'website': "http://www.palaciosdelhogar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/amortizacion.xml', 

        'views/sale_order_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
