# -*- coding: utf-8 -*-

from odoo import fields,models


class cita(models.Model):
    _name = 'upohome.cita'
    
    name = fields.Char('ID de la cita', size=9, required=True)
    fecha = fields.Datetime('Fecha y hora',required=True)
    descripcion = fields.Char('Descripcion', size=100)

