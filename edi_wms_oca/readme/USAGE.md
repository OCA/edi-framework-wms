- Go to *EDI > Config > Backend types* and check *WMS* on the
  backend types that connect to a WMS. Integration modules usually set it
  in their data.
- The backends of these types are *WMS Enabled*: set the *Warehouse* the
  WMS serves on each of them.

Developers can override `edi.backend._compute_wms_enabled()` to enable
the WMS features on other conditions.
