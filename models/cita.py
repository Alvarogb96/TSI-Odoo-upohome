# -*- coding: utf-8 -*-

from odoo import fields,models


class cita(models.Model):
    _name = 'upohome.cita'
    
    name = fields.Char('ID de la cita', size=9, required=True)
    fecha = fields.Datetime('Fecha y hora',required=True)
    descripcion = fields.Char('Descripcion', size=100)
    cliente_id = fields.Many2one('upohome.cliente', 'Cliente') 
    empleado_ids = fields.Many2one('upohome.empleado', 'Empleado') 
    vivienda_ids = fields.Many2many('upohome.vivienda', 'Viviendas')
    _sql_constraints = [('upohome_cita_name_unique','UNIQUE (name)','El ID de la cita debe ser único')]

