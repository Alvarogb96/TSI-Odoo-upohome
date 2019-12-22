# -*- coding: utf-8 -*-

from odoo import models, fields


class electricidad(models.Model):
    _inherit = 'upohome.contrato'
    
    name = fields.Char('Compañia', size = 45, required=True)
    kw = fields.Integer('KW', required=True)
    #tarifa = fields.Char('Tarifa', size = 45, required=True)
    
