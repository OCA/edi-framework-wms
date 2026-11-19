# Copyright 2026 Camptocamp SA
# @author Simone Orsi <simone.orsi@camptocamp.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class EDIBackendType(models.Model):
    _inherit = "edi.backend.type"

    wms = fields.Boolean(
        string="WMS",
        help="The backends of this type exchange with a warehouse management system.",
    )
