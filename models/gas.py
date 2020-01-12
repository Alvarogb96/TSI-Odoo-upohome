# -*- coding: utf-8 -*-

from odoo import models, fields


class gas(models.Model):
    #HERENCIA POR PROTOTIPO
    _inherit = 'upohome.contrato'
    _name = 'upohome.gas'
    
    
    tipo = fields.Selection([('butano', 'Butano'),
                              ('natural', 'natural'), ],
                              "Tipo de gas contratado", required=True)
    
