# -*- coding: utf-8 -*-
# from odoo import http


# class Garantia(http.Controller):
#     @http.route('/garantia/garantia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/garantia/garantia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('garantia.listing', {
#             'root': '/garantia/garantia',
#             'objects': http.request.env['garantia.garantia'].search([]),
#         })

#     @http.route('/garantia/garantia/objects/<model("garantia.garantia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('garantia.object', {
#             'object': obj
#         })
