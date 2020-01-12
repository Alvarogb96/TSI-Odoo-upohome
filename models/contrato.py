# -*- coding: utf-8 -*-

from odoo import fields,models


class contrato(models.Model):
    _name = 'upohome.contrato'
    
    name = fields.Integer('Número de contrato', size=6, required=True)
    compañia = fields.Char('Compañia', size = 45, required=True)
    tarifa = fields.Float("Precio medio", required = True)
    alquiler_id = fields.Many2one('upohome.alquiler', 'Alquiler')
    _sql_constraints = [('upohome_contrato_name_unique','UNIQUE (name)','El número de contrato debe ser único')]
