/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState, onWillStart, onWillUpdateProps } from "@odoo/owl";

class GoogleMapWidget extends Component {
    static template = "tr_google_maps.MapWidget";
    static props = {
        record: Object,
        readonly: { type: Boolean, optional: true },
    };

    setup() {
        this.rpc = useService("rpc");
        this.state = useState({
            apiKey: "",
            address: "",
            embedUrl: "",
            googleMapsUrl: "",
            height: 350,
        });

        onWillStart(async () => {
            await this._loadSettings();
            this._buildAddress();
        });

        onWillUpdateProps(async () => {
            this._buildAddress();
        });
    }

    async _loadSettings() {
        const result = await this.rpc("/web/dataset/call_kw", {
            model: "ir.config_parameter",
            method: "get_param",
            args: ["tr_google_maps.api_key"],
            kwargs: {},
        });
        this.state.apiKey = result || "";

        const height = await this.rpc("/web/dataset/call_kw", {
            model: "ir.config_parameter",
            method: "get_param",
            args: ["tr_google_maps.height"],
            kwargs: {},
        });
        this.state.height = parseInt(height) || 350;
    }

    _buildAddress() {
        const record = this.props.record.data;
        const parts = [
            record.street,
            record.street2,
            record.city,
            record.zip,
            record.country_id && record.country_id[1],
        ].filter(Boolean);

        const address = parts.join(", ");
        this.state.address = address;

        if (address && this.state.apiKey) {
            const encoded = encodeURIComponent(address);
            this.state.embedUrl = `https://www.google.com/maps/embed/v1/place?key=${this.state.apiKey}&q=${encoded}`;
            this.state.googleMapsUrl = `https://www.google.com/maps/search/?api=1&query=${encoded}`;
        }
    }
}

registry.category("view_widgets").add("tr_google_map", {
    component: GoogleMapWidget,
});
