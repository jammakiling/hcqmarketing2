from odoo import models, fields, api ,exceptions
import re

class EmployeeType(models.Model):
    _name = 'hcqmemployees.type'
    _description = 'Custom Employee Type'

    name = fields.Char(string='Employee Type', required=True)

class Employee(models.Model):
    _name = 'hcqmemployees.employee'
    _description = 'Custom Employee'

    name = fields.Char(string='Employee Name', required=True)
    employee_type_id = fields.Many2one('hcqmemployees.type', string='Employee Type', required=True)
    address = fields.Text(string='Address')
    contactnum = fields.Char(string='Contact Number')
    email = fields.Char(string="Email", help="Enter a valid email address")
    
    
    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email:
                match = re.match(r"[^@]+@[^@]+\.[^@]+", record.email)
                if not match:
                    raise exceptions.ValidationError("Please enter a valid email address.")
    
