# -*- coding: utf-8 -*-
# from odoo import http


# class NewDemoApp(http.Controller):
#     @http.route('/new_demo_app/new_demo_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_demo_app/new_demo_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_demo_app.listing', {
#             'root': '/new_demo_app/new_demo_app',
#             'objects': http.request.env['new_demo_app.new_demo_app'].search([]),
#         })

#     @http.route('/new_demo_app/new_demo_app/objects/<model("new_demo_app.new_demo_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_demo_app.object', {
#             'object': obj
#         })
