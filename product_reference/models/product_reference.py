from odoo import models, api, _


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        if not vals.get('default_code'):
            vals['default_code'] = self.env['ir.sequence'].next_by_code('product.template') or _('New')
        res = super(ProductTemplateInherit, self).create(vals)
        return res



