# -*- coding: utf-8 -*-
# from odoo import http


# class Nahe80mmInvoiceTicket(http.Controller):
#     @http.route('/nahe_80mm_invoice_ticket/nahe_80mm_invoice_ticket', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nahe_80mm_invoice_ticket/nahe_80mm_invoice_ticket/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nahe_80mm_invoice_ticket.listing', {
#             'root': '/nahe_80mm_invoice_ticket/nahe_80mm_invoice_ticket',
#             'objects': http.request.env['nahe_80mm_invoice_ticket.nahe_80mm_invoice_ticket'].search([]),
#         })

#     @http.route('/nahe_80mm_invoice_ticket/nahe_80mm_invoice_ticket/objects/<model("nahe_80mm_invoice_ticket.nahe_80mm_invoice_ticket"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nahe_80mm_invoice_ticket.object', {
#             'object': obj
#         })
