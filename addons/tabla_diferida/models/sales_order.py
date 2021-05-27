# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.exceptions import AccessError, UserError, ValidationError

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'



    def action_test(self):
        raise UserError('Holaaaaa')


    @api.depends('order_line.price_total')
    @api.onchange('entrada')
    def _valorentrada(self):
        """
        Compute the total amounts of the SO.
        """

        for order in self:
            amount_entrada = subt = 0.0

            amount_entrada += order.entrada
            subt += order.amount_total

            order.update({
                'amount_entrada': amount_entrada,
                'total': subt - amount_entrada,

            })

    entrada = fields.Monetary(string="Entrada", required=True )
    total = fields.Monetary(string="Total", readonly=True)
    amount_entrada = fields.Monetary(string="Entrada", readonly=True, compute='_valorentrada')
    subt = fields.Monetary(string="Subt")





