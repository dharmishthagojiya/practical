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
    date_deadline = fields.Date(string="Deadline", compute="_compute_date", inverse="_inverse_date")
    create_date = fields.Datetime(default=fields.Datetime.now())
    property_type_id = fields.Many2one(related="property_id.property_type_id",store=True)

    @api.depends("validity")
    def _compute_date(self):
        for rec in self:
            rec.date_deadline = fields.Datetime.add(rec.create_date.date(), days=rec.validity)
    def _inverse_date(self):
        fmt = '%Y-%m-%d'
        for rec in self:
            d1 = fields.datetime.strptime(str(rec.date_deadline), fmt)
            d2 = fields.datetime.strptime(str(rec.create_date.date()), fmt)
            diff = (d1-d2).days
            rec.validity = str(diff)

    '''def action_accept(self):
        self.status = 'accepted'
        self.property_id.selling_price = self.price
        self.property_id.buyer_id = self.partner_id'''
    def action_accept(self):
        refuse = self.env['test.model'].browse(self.property_id)
        refuse.refuse_offer(self.price)
        self.property_id.selling_price = self.price
        if self.property_id.selling_price != 0:
            self.status = 'accepted'
            self.property_id.buyer_id = self.partner_id
            self.property_id.state = 'offer_accepted'

    def action_reject(self):
        self.status = 'refused'

    
