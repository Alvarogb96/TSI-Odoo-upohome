# -*- coding: utf-8 -*-

from odoo import models, fields


class internet(models.Model):
    _inherit = 'upohome.contrato'
    
    name = fields.Char('Compañia', size = 45, required=True)
    #tarifa = fields.Float('Precio estimado', required=True)
    tipo = fields.Selection([('fibra', 'Fibra'),
                              ('adsl', 'ADSL'), ],
                              "Tipo de internet contratado", required=True)
    Velocidad = fields.Float("Velocidad", required=True)
