# -*- coding: utf-8 -*-

from odoo import models, fields


class electricidad(models.Model):
    #HERENCIA POR PROTOTIPO
    _inherit = 'upohome.contrato'
    _name = 'upohome.electricidad'
    
    
    kw = fields.Float('KW', required=True)
    
    
