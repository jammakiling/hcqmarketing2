from odoo import models, fields, api ,exceptions
import re

class Customer(models.Model):
    _name = "hcqmsale.customer"
    _description = "HCQ Sale Customer"

    name = fields.Char(string='Customer Name', required=True)
    address = fields.Text(string='Address')
    contactname = fields.Char(string='Contact Person')
    contactnum1 = fields.Char(string='Contact Number 1')
    contactnum2 = fields.Char(string='Contact Number 2')
    contactnum3 = fields.Char(string='Contact Number 3')
    email = fields.Char(string="Email", help="Enter a valid email address")
    ownername = fields.Char(string='Owner')
    
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                match = re.match(r"[^@]+@[^@]+\.[^@]+", record.email)
                if not match:
                    raise exceptions.ValidationError("Please enter a valid email address.")
    
