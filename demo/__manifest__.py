# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'demo',
    'version': '1.0.0',
    'category': 'Demo',
    'author': 'Aardug',
    'sequence': -100,
    'summary': 'management system',
    'description': """Odoo demo""",
    'depends': ['mail', 'product', 'sale', 'sales_team', 'contacts', 'mrp', 'account', 'base_iban', 'base_vat',
                'l10n_nl',
                'l10n_latam_invoice_document',
                'l10n_latam_base',
                'base_setup',
                'base',
                'account_edi_ubl_bis3',
                'stock',
                'resource',
                'barcodes',
                'base_setup',
                'analytic',
                'purchase_stock',
                ],
    'data': [
        'data/data.xml',
        'data/data_bills.xml',
        'data/data_products.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
