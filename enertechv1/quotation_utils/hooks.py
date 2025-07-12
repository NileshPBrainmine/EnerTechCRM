# enertechv1/quotation_utils/hooks.py

import frappe
from frappe.utils import nowdate

def set_sent_date(doc, method):
    if not doc.quotation_sent_date:
        doc.custom_quotation_sent_date = nowdate()
