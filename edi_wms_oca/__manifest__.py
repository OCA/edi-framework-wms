# Copyright 2026 Camptocamp SA
# @author Simone Orsi <simone.orsi@camptocamp.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "EDI WMS",
    "summary": "Base for the exchanges with a warehouse management system",
    "version": "19.0.1.0.0",
    "category": "EDI",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/edi-framework-wms",
    "license": "LGPL-3",
    "maintainers": ["simahawk"],
    "depends": [
        "edi_core_oca",
        "stock",
    ],
    "data": [
        "views/edi_backend_type_views.xml",
        "views/edi_backend_views.xml",
    ],
}
