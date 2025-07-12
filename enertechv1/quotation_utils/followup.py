# enertechv1/quotation_utils/followup.py

import frappe
from frappe.utils import nowdate, add_days

def send_client_followup():
    followup_day = add_days(nowdate(), -3)

    quotations = frappe.get_all("Quotation",
        filters={
            "custom_quotation_sent_date": followup_day,
            "status": "Submitted"
        },
        fields=["name", "customer_name", "email_id"]
    )

    for q in quotations:
        if not q.email_id:
            continue

        message = f"""
        Dear {q.customer_name},

        Just following up on the quotation we shared (Quotation ID: {q.name}) 3 days ago.

        Please let us know your thoughts, and feel free to reply to this email if you have any questions.

        Best Regards,  
        EnerTech Sales Team
        """

        frappe.sendmail(
            recipients=[q.email_id],
            subject=f"Follow-up on Quotation {q.name}",
            message=message
        )

        # Log email in Communication timeline
        frappe.get_doc({
            "doctype": "Communication",
            "subject": f"Follow-up Email Sent for Quotation {q.name}",
            "content": message,
            "sent_or_received": "Sent",
            "reference_doctype": "Quotation",
            "reference_name": q.name,
            "communication_type": "Communication",
        }).insert(ignore_permissions=True)
