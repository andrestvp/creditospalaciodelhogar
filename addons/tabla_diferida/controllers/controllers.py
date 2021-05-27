# -*- coding: utf-8 -*-
# from odoo import http


# class TablaDiferida(http.Controller):
#     @http.route('/tabla_diferida/tabla_diferida/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tabla_diferida/tabla_diferida/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tabla_diferida.listing', {
#             'root': '/tabla_diferida/tabla_diferida',
#             'objects': http.request.env['tabla_diferida.tabla_diferida'].search([]),
#         })

#     @http.route('/tabla_diferida/tabla_diferida/objects/<model("tabla_diferida.tabla_diferida"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tabla_diferida.object', {
#             'object': obj
#         })
