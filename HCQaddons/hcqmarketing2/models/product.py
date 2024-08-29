from odoo import models, fields, api

class Product(models.Model):
    _name = "hcqminventory.product"
    _description = "HCQ Inventory Product"

    name = fields.Char(string='Product Name', required=True)
    image = fields.Image(string='Product Image')
    description = fields.Text(string='Description')
    brand_id = fields.Many2one('hcqminventory.productbrand', string='Brand')
    category_id = fields.Many2one('hcqminventory.productcategory', string='Category')
    list_price_1 = fields.Float(string='List Price 1')
    list_price_2 = fields.Float(string='List Price 2')
    list_price_3 = fields.Float(string='List Price 3')
    list_price_4 = fields.Float(string='List Price 4')
    cost_price = fields.Float(string='Cost Price')

class ProductBrand(models.Model):
    _name = 'hcqminventory.productbrand'
    _description = 'Product Brand'

    name = fields.Char(string='Brand Name', required=True)

class ProductCategory(models.Model):
    _name = 'hcqminventory.productcategory'
    _description = 'Product Category'

    name = fields.Char(string='Category', required=True)