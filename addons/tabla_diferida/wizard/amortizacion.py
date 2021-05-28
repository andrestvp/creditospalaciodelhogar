from odoo import models, fields, api

class wizard(models.TransientModel):
    _name='create.appointment.wizard'

    ejemplo = fields.Monetary(string="Ejemplo")
