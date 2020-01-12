# -*- coding: utf-8 -*-

from odoo import fields, models


class propietario(models.Model):
    _name = 'upohome.propietario'
    
    name = fields.Char('DNI', size=9, required=True)
    nombre = fields.Char('Nombre', size=60, required=True)
    apellidos = fields.Char('Apellidos', size=60, required=True) 
    telefono = fields.Char('Telefono', size=9, required=True)
    vivienda_ids = fields.One2many('upohome.vivienda', 'propietario_id', 'Vivienda')
