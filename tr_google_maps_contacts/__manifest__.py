{
    'name': 'Google Maps on Contacts',
    'version': '19.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Show Google Maps location on Contact, Customer and Vendor forms',
    'description': """
Google Maps on Contacts — by Vayu Sharma
=============================================
Displays an interactive Google Maps view directly on the contact form.

Features:
- Google Maps embedded on Contact / Customer / Vendor form
- Auto-loads map based on partner address
- Configurable API key in Settings
- Open in Google Maps button
- Works for Companies and Individuals
- Street View support
    """,
    'author': 'Vayu Sharma',
    'website': '',
    'license': 'OPL-1',
    'depends': ['contacts', 'base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'tr_google_maps_contacts/static/src/css/google_maps.css',
            'tr_google_maps_contacts/static/src/xml/google_maps_widget.xml',
            'tr_google_maps_contacts/static/src/js/google_maps_widget.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 9.00,
    'currency': 'USD',
}
