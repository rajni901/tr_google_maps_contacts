from urllib.parse import quote
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    google_map_url = fields.Char(
        string='Google Maps URL',
        compute='_compute_google_map_url',
    )
    google_map_embed_url = fields.Char(
        string='Google Maps Embed URL',
        compute='_compute_google_map_url',
    )

    def _compute_google_map_url(self):
        api_key = self.env['ir.config_parameter'].sudo().get_param('tr_google_maps.api_key', '')
        for partner in self:
            parts = [
                partner.street,
                partner.street2,
                partner.city,
                partner.zip,
                partner.country_id.name if partner.country_id else '',
            ]
            address = ', '.join(p for p in parts if p)
            if address:
                encoded = quote(address)
                partner.google_map_url = f'https://www.google.com/maps/search/?api=1&query={encoded}'
                if api_key:
                    partner.google_map_embed_url = f'https://www.google.com/maps/embed/v1/place?key={api_key}&q={encoded}'
                else:
                    partner.google_map_embed_url = False
            else:
                partner.google_map_url = False
                partner.google_map_embed_url = False
