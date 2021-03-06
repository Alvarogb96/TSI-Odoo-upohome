# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vivienda(models.Model):
    _name = 'upohome.vivienda'
    
    name = fields.Char('ID vivienda', size=5, required=True)
    direccion = fields.Char('Dirección', size=60, required=True)
    precioAlquiler = fields.Float("Precio alquiler", required=True) 
    state = fields.Selection([('alquilada', 'Alquilada'),
                              ('noAlquilada', 'No alquilada'),
                              ('limpiando','Limpiando'),],
                              "Estado", default='noAlquilada')
    imagenPrincipal = fields.Binary('Imagen') 
    numHabitaciones = fields.Integer("Numero de habitaciones",required=True)
    descripcion = fields.Char('Descripcion', size=100, required=True)
    exterior = fields.Selection([('si', 'Sí'),
                                     ('no', 'No'), ],
                                     'Exterior')
    climatizacion = fields.Selection([('si', 'Sí'),
                                     ('no', 'No'), ],
                                     'Climatizacion')
    alquiler_ids = fields.One2many('upohome.alquiler', 'vivienda_id', 'Alquileres')
    cita_ids = fields.Many2many('upohome.cita', string='Citas para ver la vivienda')
    reforma_ids = fields.One2many('upohome.reforma', 'vivienda_id', 'Reformas')
    propietario_id = fields.Many2one('upohome.propietario', 'Propietario')
    limpieza_ids = fields.One2many('upohome.limpieza', 'vivienda_id', 'Limpiezas')
    galeria_id = fields.Many2one('upohome.galeria', 'Galeria')
    _sql_constraints = [('upohome_vivienda_name_unique','UNIQUE (name)','El ID vivienda debe ser único')]
    
    #WORKFLOWS
    @api.one
    def btn_submit_to_alquilada(self):
        self.write({'state':'alquilada'})
        
    @api.one
    def btn_submit_to_noAlquilada(self):
        self.write({'state':'noAlquilada'})
        
    @api.one
    def btn_submit_to_limpiando(self):
        self.write({'state':'limpiando'})
        
    @api.one 
    @api.constrains('precioAlquiler')
    def check_precioAlquiler(self):
        if self.precioAlquiler <= 0.0 : 
            raise models.ValidationError('El precio de alquiler debe ser superior a 0')
        
    @api.onchange('alquiler_ids')
    def onchange_alquiler(self):
        if self.state != 'noAlquilada':
            raise models.ValidationError('La vivienda no está disponible para ser alquilada.')
    
    @api.onchange('limpieza_ids')
    def onchange_limpieza(self):
        self.state = 'limpiando'