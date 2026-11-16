# Copyright 2026 Camptocamp SA
# @author Simone Orsi <simone.orsi@camptocamp.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.tests.common import TransactionCase


class TestEdiBackend(TransactionCase):
    """The backends of a WMS backend type are WMS enabled."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.wms_type = cls.env["edi.backend.type"].create(
            {"name": "Test WMS", "code": "test_edi_wms_oca_wms", "wms": True}
        )
        cls.other_type = cls.env["edi.backend.type"].create(
            {"name": "Test Other", "code": "test_edi_wms_oca_other"}
        )
        cls.wms_backend = cls.env["edi.backend"].create(
            {"name": "Test WMS", "backend_type_id": cls.wms_type.id}
        )
        cls.other_backend = cls.env["edi.backend"].create(
            {"name": "Test Other", "backend_type_id": cls.other_type.id}
        )

    def test_wms_enabled(self):
        """A backend of a WMS type is WMS enabled, one of another type is not."""
        self.assertTrue(self.wms_backend.backend_type_wms)
        self.assertTrue(self.wms_backend.wms_enabled)
        self.assertFalse(self.other_backend.wms_enabled)

    def test_wms_enabled_follows_type(self):
        """Flagging the backend type as WMS enables its backends."""
        self.other_type.wms = True
        self.assertTrue(self.other_backend.wms_enabled)
        self.wms_type.wms = False
        self.assertFalse(self.wms_backend.wms_enabled)

    def test_backend_type_change(self):
        """A backend moved to a WMS type becomes WMS enabled."""
        self.other_backend.backend_type_id = self.wms_type
        self.assertTrue(self.other_backend.wms_enabled)
