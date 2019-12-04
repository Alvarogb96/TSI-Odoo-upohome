# -*- coding: utf-8 -*-

from odoo import models, fields


class alquiler(models.Model):
    _name = 'upohome.alquiler'
    
    name = fields.Char('ID alquiler', size=60, required=True)
    fechaInicio = fields.Datetime('Fecha de inicio', required=True)
    fechaFin = fields.Datetime('Fecha fin', required=True) 
    cliente_id = fields.Many2one('upohome.cliente', 'Cliente') 
    vivienda_id = fields.Many2one('upohome.vivienda', 'Vivienda')
    
    
    