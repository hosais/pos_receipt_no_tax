/** @odoo-module **/
import { ReceiptScreen } from 'point_of_sale.ReceiptScreen';
import { patch } from "@web/core/utils/patch";

import { templates } from 'web.owl';
import { xml } from "@odoo/owl";

import receiptTemplate from 'pos_receipt_no_tax_js/static/src/xml/pos_receipt_template.xml';

patch(ReceiptScreen.prototype, {
    setup() {
        super.setup();
        // Use our patched template
        this.template = receiptTemplate;
    },
});