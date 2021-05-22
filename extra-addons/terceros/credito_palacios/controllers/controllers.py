# -*- coding: utf-8 -*-
# from odoo import http


# class CreditoPalacios(http.Controller):
#     @http.route('/credito_palacios/credito_palacios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/credito_palacios/credito_palacios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('credito_palacios.listing', {
#             'root': '/credito_palacios/credito_palacios',
#             'objects': http.request.env['credito_palacios.credito_palacios'].search([]),
#         })

#     @http.route('/credito_palacios/credito_palacios/objects/<model("credito_palacios.credito_palacios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('credito_palacios.object', {
#             'object': obj
#         })
