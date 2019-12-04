# -*- coding: utf-8 -*-

from odoo import models, fields


class galeria(models.Model):
    _name = 'upohome.galeria'
    
    imagen1 = fields.Binary('Imagen 1')
    imagen2 = fields.Binary('Imagen 2')
    imagen3 = fields.Binary('Imagen 3')
    imagen4 = fields.Binary('Imagen 4')
    imagen5 = fields.Binary('Imagen 5')
    descripcion = fields.Char('Descripcion', size=100, required=True)