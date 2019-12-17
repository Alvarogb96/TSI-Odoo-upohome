# -*- coding: utf-8 -*-

from odoo import models, fields


class agua(models.Model):
    _name = 'upohome.agua'
    
    name = fields.Char('Compañia', size = 45, required=True)
    tarifa = fields.Float('Precio estimado', required=True)