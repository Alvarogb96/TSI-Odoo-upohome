# -*- coding: utf-8 -*-

from odoo import fields,models


class reforma(models.Model):
    _name = 'upohome.reforma'
    
    name = fields.Char('ID de la reforma', size=9, required=True)
    añoReforma = fields.Integer("Año de la reforma",required=True)
    partes = fields.Char('Partes reformadas', size=100,required=True)
    coste = fields.Float("Coste de la reforma",required=True)
    vivienda_ids = fields.Many2one('upohome.vivienda', 'Vivienda')
    _sql_constraints = [('upohome_reforma_name_unique','UNIQUE (name)','El ID de la reforma debe ser único')]
