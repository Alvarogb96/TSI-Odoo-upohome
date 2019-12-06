# -*- coding: utf-8 -*-

from odoo import fields,models


class contrato(models.Model):
    _name = 'upohome.contrato'
    
    name = fields.Integer('Número de contrato', size=6, required=True)
    precioMedio = fields.Float("Precio medio", required = True)
    alquiler_id = fields.Many2one('upohome.alquiler', 'Alquiler')
