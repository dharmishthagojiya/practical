
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models,api

class TestModel(models.Model):
    _name = "test.model"  #estate_property
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Test Model"

    name = fields.Char(required=True,string="Title")
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
    garden_orientation = fields.Selection(string='Garden Orientation', selection=[('north', 'North'), ('south', 'South'), ('east', 'East'),
                                                     ('west', 'West')], default='north')
    
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, tracking=True, copy=False)
    seller_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name="estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Float(compute="_compute_total",string="total area")
    best_price = fields.Float(compute="_compute_price",string="Best offer")
    

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden==True:
            self.garden_area = 10
            self.garden_orientation = 'north'

    @api.depends("living_area","garden_area")
    def _compute_total(self):
        self.total_area = self.living_area + self.garden_area

    @api.depends("offer_ids.partner_id")
    def _compute_price(self):
        if self.offer_ids.partner_id:
            self.best_price = max(i.price for i in self.offer_ids)
        else:
            self.best_price = 0
