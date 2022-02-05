
from odoo import api, fields, models

class TestModel(models.Model):
    _name = "test.model"  #estate_property
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Test Model"

    name = fields.Char(string="Title", required=True, tracking=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From', copy=False, default=lambda self: fields.Datetime.add(fields.Datetime.now(),months=3))
    expected_price = fields.Float(required=True, string='Expected Price', tracking=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(default=2, string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('north', 'North'), ('south', 'South'), ('east', 'East'),('west', 'West')])
    state = fields.Selection(string="State", selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')], default='new', tracking=True)
    active = fields.Boolean(string="Active", default=True)
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    seller_id = fields.Many2one('res.partner', string='Salesperson', index=True, tracking=True,
                              default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.users', string='Buyer', index=True, tracking=True, copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "partner_id", string="Offers")
    total_area = fields.Float(compute="_compute_total", string="Total Area (sqm)")
    best_price = fields.Integer(default="0", string="Best Offer")

    def action_received(self):
        self.state = 'offer_received'

    def action_accepted(self):
        self.state = 'offer_accepted'

    def action_sold(self):
        self.state = 'sold'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_new(self):
        self.state = 'new'

    @api.model
    def create(self, vals):
        if not vals.get('description'):
            vals['description'] = 'New Property'
        res = super(TestModel, self).create(vals)
        return res

    @api.depends('living_area', 'garden_area')
    def _compute_total(self):
        self.total_area = self.living_area + self.garden_area

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden==True:
            self.garden_area = 10
            self.garden_orientation = 'north'
'''
    @api.depends("offer_ids.partner_id")
    def _compute_price(self):
        if self.offer_ids.partner_id is not None:
            self.best_price = max(i.price for i in self.offer_ids)
'''
