# -*- coding: utf-8 -*-

from odoo import models, fields


class electricidad(models.Model):
    _name = 'upohome.electricidad'
    
    name = fields.Integer('KW', required=True)
    tarifa = fields.Char('Tarifa', size = 45, required=True)
    compañia = fields.Char('Compañia', size = 45, required=True)