# -*- coding: utf-8 -*-



#from datetime import datetime, timedelta
#from functools import partial
#from itertools import groupby
#from odoo.exceptions import AccessError, UserError, ValidationError
#from odoo.tools.misc import formatLang, get_lang
#from odoo.osv import expression
#from odoo.tools import float_is_zero, float_compare


#from werkzeug.urls import url_encode
from odoo import  api, fields, models
from odoo.exceptions import AccessError, UserError, ValidationError


class CreaAmortizacion(models.Model):
    _name = 'visualiza.amortizacion'
    #_inherit = "sale.order"



    #totalpagar = fields.Float(string="Total Pagar")
    mes = fields.Char(string="Mes")
    cuota = fields.Float(string="Cuota")

  


    mes1 = fields.Char(string="Mes")
    cuota1 = fields.Char(string="Cuota")
    observacion = fields.Text(string="Observación")
    amor_id =fields.One2many('table.amor','relacion',string="Amort")

    totalpagar = fields.Float(string="Total Pagar")


    def imprimir(self):
        raise UserError('Holaaaaa y')


class Prueba(models.Model):
    _name = 'table.amor'
    _description = "Prueba"

   
    relacion = fields.Many2one ('sale.order',string='Probando', readonly=True)
    numero = fields.Integer(string='Nº', readonly=True)
    fecha = fields.Date(string='Fecha Vencimiento', readonly=True)
    pagos = fields.Float(string="Pagos", readonly=True)
    amortizacion = fields.Float(string="Amortización", readonly=True)
    interes = fields.Float(string="Interés", readonly=True)
    capital = fields.Float(string='Capital')
    saldo = fields.Float(string='Saldo')
    detalle = fields.Float(string='Detalle')

    
    
