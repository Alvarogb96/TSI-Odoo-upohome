# -*- coding: utf-8 -*-

from odoo import models, fields


class agua(models.Model):
    _inherit = 'upohome.contrato'
    
    name = fields.Char('Compañia', size = 45, required=True)
    tarifa = fields.Float('Precio estimado', required=True)