# -*- coding: utf-8 -*-

from odoo import models, fields


class gas(models.Model):
    _inherit = 'upohome.contrato'
    
    name = fields.Char('Compañia', size = 45, required=True)
    #tarifa = fields.Char('Tarifa', size = 65, required=True)
