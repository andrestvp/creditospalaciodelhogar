# -*- coding: utf-8 -*-
# from odoo import http


# class Credito-palacios(http.Controller):
#     @http.route('/credito-palacios/credito-palacios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/credito-palacios/credito-palacios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('credito-palacios.listing', {
#             'root': '/credito-palacios/credito-palacios',
#             'objects': http.request.env['credito-palacios.credito-palacios'].search([]),
#         })

#     @http.route('/credito-palacios/credito-palacios/objects/<model("credito-palacios.credito-palacios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('credito-palacios.object', {
#             'object': obj
#         })
