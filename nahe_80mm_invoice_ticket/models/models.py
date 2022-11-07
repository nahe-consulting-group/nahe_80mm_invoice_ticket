# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nahe_80mm_invoice_ticket(models.Model):
#     _name = 'nahe_80mm_invoice_ticket.nahe_80mm_invoice_ticket'
#     _description = 'nahe_80mm_invoice_ticket.nahe_80mm_invoice_ticket'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
