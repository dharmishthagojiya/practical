from odoo import fields, models


class TestModel(models.Model):
    _name = "estate.property.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property Type"

    name = fields.Char(string="Property Type", required=True, tracking=True)
    property_ids = fields.One2many('test.model','property_type_id',string="Property")
    sequence = fields.Integer('Sequence', default=1)
