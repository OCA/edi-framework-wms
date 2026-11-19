# Copyright 2026 Camptocamp SA
# @author Simone Orsi <simone.orsi@camptocamp.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class EDIBackend(models.Model):
    _inherit = "edi.backend"

    warehouse_id = fields.Many2one("stock.warehouse")
    backend_type_wms = fields.Boolean(related="backend_type_id.wms")
    wms_enabled = fields.Boolean(
        string="WMS Enabled",
        compute="_compute_wms_enabled",
        store=True,
        precompute=True,
        help="The backend exchanges with a warehouse management system: the WMS "
        "rules apply to the records it exports.",
    )

    @api.depends("backend_type_wms")
    def _compute_wms_enabled(self):
        """Enable the WMS features on the backends of a WMS backend type.

        Override it to enable them on other conditions.
        """
        for backend in self:
            backend.wms_enabled = backend.backend_type_wms
