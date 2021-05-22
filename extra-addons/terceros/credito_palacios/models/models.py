# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class credito_palacios(models.Model):
#     _name = 'credito_palacios.credito_palacios'
#     _description = 'credito_palacios.credito_palacios'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
