# -*- coding: utf-8 -*-

from odoo import fields,models


class limpieza(models.Model):
    _name = 'upohome.limpieza'
    
    name = fields.Char('ID de la limpieza', size=9, required=True)
    fecha = fields.Datetime('Fecha y hora',required=True)
    finalizado = fields.Selection([('si','Sí'),
                                     ('no','No'),],
                                     'Finalizado')
    empleado_ids = fields.Many2one('upohome.empleado','Empleado')