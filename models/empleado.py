# -*- coding: utf-8 -*-

from odoo import fields, models


class empleado(models.Model):
    _name = 'upohome.empleado'
    
    name = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=60, required=True) 
    telefono = fields.Char('Telefono', size=9, required=True)
    salario = fields.Float("Salario", required=True)
    domicilio = fields.Char('Domicilio', size=65, required=True)
    cita_ids = fields.One2many('upohome.cita', 'cliente_id', 'Citas')
    limpieza_ids = fields.One2many('upohome.limpieza', 'empleado_ids', 'Limpieza')
