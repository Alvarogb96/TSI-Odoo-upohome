# -*- coding: utf-8 -*-

from odoo import models, fields


class galeria(models.Model):
    _name = 'upohome.galeria'
    
    #falta relación one2one
    imagen1 = fields.Binary('Imagen 1', required=False )
    descripcion1 = fields.Char('Descripcion', size=85, required=False)
    imagen2 = fields.Binary('Imagen 2', required=False)
    descripcion2 = fields.Char('Descripcion', size=85, required=False)
    imagen3 = fields.Binary('Imagen 3', required=False)
    descripcion3 = fields.Char('Descripcion', size=85, required=False)
    imagen4 = fields.Binary('Imagen 4', required=False)
    descripcion4 = fields.Char('Descripcion', size=85, required=False)
    imagen5 = fields.Binary('Imagen 5', required=False)
    descripcion5 = fields.Char('Descripcion', size=85, required=False)
    vivienda_ids = fields.Many2one('upohome.vivienda', 'Vivienda')