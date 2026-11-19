A project exchanging with a WMS needs rules that other EDI exchanges of
the same records must not get: e.g. a transfer can be sent to the WMS
only once, and only while it is waiting or ready, while a despatch advice
is sent for the same transfer once it is done.

The integration modules for a given WMS define its backend type: this
module lets them flag it, so the generic WMS modules never depend on a
backend type code.
