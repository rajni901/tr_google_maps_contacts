/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

class GoogleMapIframe extends Component {
    static template = "tr_google_maps.IframeWidget";
    static props = {
        ...standardFieldProps,
    };

    get embedUrl() {
        return this.props.record.data.google_map_embed_url || "";
    }

    get mapUrl() {
        return this.props.record.data.google_map_url || "";
    }

    get hasAddress() {
        return !!this.props.record.data.google_map_url;
    }

    get hasApiKey() {
        return !!this.props.record.data.google_map_embed_url;
    }
}

registry.category("fields").add("tr_google_map_iframe", {
    component: GoogleMapIframe,
    supportedTypes: ["char"],
});
