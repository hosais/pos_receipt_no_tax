{
    "name": "POS Receipt No Tax",
    "version": "15.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Removes tax info from POS frontend receipt using OWL template override",
    "author": "TZ hosais CJL",
    "website": "https://github.com/hosais/pos_receipt_no_tax",
    "depends": [
        "point_of_sale",
        "ba_dcp_pos_extension"
    ],
    "assets": {
        "web.assets_qweb": [
            "pos_receipt_no_tax_js/static/src/xml/OrderReceipt.xml",
            'pos_receipt_no_tax/static/src/xml/ba_dcp_history_button.xml',
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
