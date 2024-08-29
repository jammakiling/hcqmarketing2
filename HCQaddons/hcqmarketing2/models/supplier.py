from odoo import models, fields, api ,exceptions
import re

class Supplier(models.Model):
    _name = "hcqminventory.supplier"
    _description = "HCQ Inventory Supplier"

    name = fields.Char(string='Supplier Name', required=True)
    address = fields.Text(string='Address')
    contactname = fields.Char(string='Contact Person')
    contactnum = fields.Char(string='Contact Number')
    secretaryname = fields.Char(string='Secretary')
    secretarynum = fields.Char(string='Secretary Number')
    email = fields.Char(string="Email", help="Enter a valid email address")
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                match = re.match(r"[^@]+@[^@]+\.[^@]+", record.email)
                if not match:
                    raise exceptions.ValidationError("Please enter a valid email address.")
    
