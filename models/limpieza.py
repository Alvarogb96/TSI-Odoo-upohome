# -*- coding: utf-8 -*-

from odoo import fields,models


class limpieza(models.Model):
    _name = 'upohome.limpieza'
    
    name = fields.Char('ID de la limpieza', size=9, required=True)
    fecha = fields.Datetime('Fecha y hora',required=True)
    finalizado = fields.Selection([('si','Sí'),
                                     ('no','No'),],
                                     'Finalizado')
    empleado_id = fields.Many2one('upohome.empleado','Empleado')
    vivienda_id = fields.Many2one('upohome.vivienda', 'Vivienda')
    
    _sql_constraints = [('upohome_limpieza_name_unique','UNIQUE (name)','El ID de limpieza debe ser único')]