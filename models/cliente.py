# -*- coding: utf-8 -*-

from odoo import fields, models


class cliente(models.Model):
    _name = 'upohome.cliente'
    
    name = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=60, required=True) 
    telefono = fields.Char('Telefono', size=9, required=True)
    domicilio = fields.Char('Domicilio', size=65, required=True)
    alquiler_ids = fields.One2many('upohome.alquiler', 'cliente_id', 'Alquileres')
    cita_ids = fields.One2many('upohome.cita', 'cliente_id', 'Citas')
    _sql_constraints = [('upohome_cliente_name_unique','UNIQUE (name)','El DNI debe ser único')]
    
