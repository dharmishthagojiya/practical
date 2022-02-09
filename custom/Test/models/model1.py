# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models,api
from odoo.exceptions import ValidationError

class TestModel(models.Model):
    _name = "test.model"  #estate_property
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Test Model"

    name = fields.Char(required=True,string="Name")
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From')
    expected_price = fields.Float(required=True, string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(default=2, string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('north', 'North'), ('south', 'South'), ('east', 'East'),
                                                     ('west', 'West')], default='north')
    
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, tracking=True, copy=False)
    seller_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name="estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total",string="total area")
    best_price = fields.Float(compute="_compute_price",string="Best offer")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(string="State", selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')], default='new', tracking=True)
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected price of a property should be greater than 0.'),
        ('check_selling_price', 'CHECK(selling_price >= 0)',
         'The selling price of a property should be positive.')
    ]

   
    @api.depends("living_area","garden_area")
    def _compute_total(self):
        self.total_area = self.living_area + self.garden_area

    @api.depends("offer_ids.partner_id")
    def _compute_price(self):
        if self.offer_ids.partner_id:
            self.best_price = max(i.price for i in self.offer_ids)
        else:
            self.best_price = 0

    @api.constrains('name')
    def check_name(self):
        for record in self:
             name = self.env['test.model'].search([('name', "=",record.name),('id','!=',record.id)])
             if name:
                raise ValidationError( ("Name  %s Already exists" % record.name))

    @api.constrains('name', 'description')
    def _check_description(self):
        for record in self:
             if record.name == record.description:
                  raise ValidationError("Fields name and description must be different")

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden == True:
            self.garden_area = 10
            self.garden_orientation = 'north'

        elif self.garden is False:
            self.garden_area = 0
            self.garden_orientation = ''

    @api.constrains('selling_price', 'expected_price')
    def _check_percent(self):
        for term_line in self:
            if term_line.expected_price == 'percent' and (term_line.selling_price < 0.0 or term_line.selling_price > 90.0):
                raise ValidationError(_('Percentages on the Payment Terms lines must be  0 to 90.'))

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
 
    @api.constrains('selling_price', 'expected_price')
    def _check_selling_price(self):
        for rec in self:
            if rec.selling_price != 0:
                value = 0.9 * rec.expected_price
                if rec.selling_price < value:
                    rec.selling_price = 0
                    raise ValidationError("The selling price should not be less than 90% of expected price.")



    '''def refuse_offer(self, price):
        # current = self.env['estate.property.offer'].browse(self._context.get('active_id')).offer_ids
        for rec in self.offer_ids:
            if rec.price == price:
                pass
            rec.action_reject()
        return True
'''

    


