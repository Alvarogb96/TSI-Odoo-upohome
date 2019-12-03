# -*- coding: utf-8 -*-
from odoo import http

# class Upohome(http.Controller):
#     @http.route('/upohome/upohome/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upohome/upohome/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upohome.listing', {
#             'root': '/upohome/upohome',
#             'objects': http.request.env['upohome.upohome'].search([]),
#         })

#     @http.route('/upohome/upohome/objects/<model("upohome.upohome"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upohome.object', {
#             'object': obj
#         })