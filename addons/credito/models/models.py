# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class credito(models.Model):
#     _name = 'credito.credito'
#     _description = 'credito.credito'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class  credito(models.MOdel):
    _name = 'credito.credito'
    _descripcion = 'credito.credito'

    name = fields.Char(string, required = True)


