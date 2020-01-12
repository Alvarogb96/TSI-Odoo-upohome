# -*- coding: utf-8 -*-

from odoo import models, fields


class internet(models.Model):
    #HERENCIA POR PROTOTIPO
    _inherit = 'upohome.contrato'
    _name = 'upohome.internet'
    
    tipo = fields.Selection([('fibra', 'Fibra'),
                              ('adsl', 'ADSL'), ],
                              "Tipo de internet contratado", required=True)
    Velocidad = fields.Float("Velocidad", required=True)
