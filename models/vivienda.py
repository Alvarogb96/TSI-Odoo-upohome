# -*- coding: utf-8 -*-

from odoo import models, fields


class vivienda(models.Model):
    _name = 'upohome.vivienda'
    
    name = fields.Char('ID vivienda', size=35, required=True)
    direccion = fields.Char('Dirección', size=60, required=True)
    precioAlquiler = fields.Float("Precio alquiler") 
    estadoDeDisponibilidad = fields.Selection([('alquilada','Alquilada'),
                                     ('no alquilada','No alquilada'),
                                     ('en reforma','En reforma'),],
                                     'Estado de disponibilidad')
    imagenPrincipal = fields.Binary('Imagen') 
    numHabitaciones = fields.Integer("Numero de habitaciones")
    descripcion = fields.Char('Descripcion', size=100, required=True)
    exterior = fields.Selection([('si','Sí'),
                                     ('no','No'),],
                                     'Exterior')
    climatizacion = fields.Selection([('si','Sí'),
                                     ('no','No'),],
                                     'Climatizacion')
    alquiler_ids = fields.One2many('upohome.alquiler','vivienda_id', 'Alquileres')
   
