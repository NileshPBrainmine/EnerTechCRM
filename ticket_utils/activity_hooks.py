import frappe
from frappe.utils import now_datetime

def update_last_activity(doc, method=None):
    # If Ticket is updated
    if doc.doctype == "Ticket":
        frappe.db.set_value("Ticket", doc.name, "custom_last_activity_time", now_datetime())

    # If comment added to a Ticket
    elif doc.reference_doctype == "Ticket":
        frappe.db.set_value("Ticket", doc.reference_name, "custom_last_activity_time", now_datetime())
