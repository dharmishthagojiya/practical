from odoo import api, fields, models


class TestModel(models.Model):
    _name = "estate.property.offer"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Property Offer"

    price = fields.Float(string="Price", tracking=True)
    status = fields.Selection(string="Status", selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('test.model', required=True)
    validity = fields.Integer(string="Validity (days)", default="7")
    date_deadline = fields.Date(string="Deadline", compute="_compute_date", store=True)

    @api.depends("validity")
    def _compute_date(self):
        self.date_deadline = fields.Date.add(self.create_date, days=self.validity)

    def _inverse_date(self):
        self.validity = fields.Date.subtract(self.date_deadline, self.create_date)
