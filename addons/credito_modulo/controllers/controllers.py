# -*- coding: utf-8 -*-
# from odoo import http


# class CreditoModulo(http.Controller):
#     @http.route('/credito_modulo/credito_modulo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/credito_modulo/credito_modulo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('credito_modulo.listing', {
#             'root': '/credito_modulo/credito_modulo',
#             'objects': http.request.env['credito_modulo.credito_modulo'].search([]),
#         })

#     @http.route('/credito_modulo/credito_modulo/objects/<model("credito_modulo.credito_modulo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('credito_modulo.object', {
#             'object': obj
#         })
