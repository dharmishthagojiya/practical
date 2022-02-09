from odoo import fields, models


class TestModel(models.Model):
    _name = "estate.property.tag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property Type"

    name = fields.Char(string="Name", required=True, tracking=True)
    color = fields.Integer()
