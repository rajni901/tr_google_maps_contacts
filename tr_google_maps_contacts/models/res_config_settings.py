from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_maps_api_key = fields.Char(
        string='Google Maps API Key',
        config_parameter='tr_google_maps.api_key',
        help='Get your API key from https://console.cloud.google.com',
    )
    google_maps_zoom = fields.Integer(
        string='Default Zoom Level',
        config_parameter='tr_google_maps.zoom',
        default=15,
    )
    google_maps_height = fields.Integer(
        string='Map Height (px)',
        config_parameter='tr_google_maps.height',
        default=350,
    )
