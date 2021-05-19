# -*- coding: utf-8 -*-
# from odoo import http


# class Cobranzas(http.Controller):
#     @http.route('/cobranzas/cobranzas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cobranzas/cobranzas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cobranzas.listing', {
#             'root': '/cobranzas/cobranzas',
#             'objects': http.request.env['cobranzas.cobranzas'].search([]),
#         })

#     @http.route('/cobranzas/cobranzas/objects/<model("cobranzas.cobranzas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cobranzas.object', {
#             'object': obj
#         })
