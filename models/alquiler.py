# -*- coding: utf-8 -*-

from odoo import models, fields


class alquiler(models.Model):
    _name = 'upohome.alquiler'
    
    name = fields.Char('ID alquiler', size=60, required=True)
    fechaInicio = fields.Datetime('Fecha de inicio', required=True)
    fechaFin = fields.Datetime('Fecha fin', required=True) 
    cliente_id = fields.Many2one('upohome.cliente', 'Cliente') 
    vivienda_id = fields.Many2one('upohome.vivienda', 'Vivienda')
    contrato_ids = fields.One2many('upohome.contrato', 'alquiler_id', 'Contratos')
    _sql_constraints = [('upohome_alquiler_name_unique','UNIQUE (name)','El ID alquiler debe ser único')]
    
