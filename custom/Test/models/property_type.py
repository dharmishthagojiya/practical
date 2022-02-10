from odoo import fields, models,api


class TestModel(models.Model):
    _name = "estate.property.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property Type"

    name = fields.Char(string="Property Type", required=True, tracking=True)
    property_ids = fields.One2many('test.model','property_type_id',string="Property")
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many('estate.property.offer','property_type_id',string="offerids")
    offer_count = fields.Integer(compute="_compute_offers")

    @api.depends('offer_ids')
    def _compute_offers(self):
        self.offer_count = len(self.offer_ids)
    
