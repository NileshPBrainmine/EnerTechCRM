import frappe
from frappe.utils import now_datetime, add_hours

def notify_inactive_tickets():
    threshold = add_hours(now_datetime(), -24)

    tickets = frappe.get_all("Ticket",
        filters={
            "custom_last_activity_time": ("<", threshold),
            "status": ["!=", "Closed"]
        },
        fields=["name", "owner", "subject"]
    )

    for ticket in tickets:
        if ticket.owner:
            frappe.sendmail(
                recipients=[ticket.owner],
                subject=f"⚠️ Inactive Ticket: {ticket.name}",
                message=f"""
                    <p>Hello,</p>
                    <p>No activity was recorded on Ticket <b>{ticket.name}</b> in the last 24 hours.</p>
                    <p>Please follow up or update the ticket.</p>
                """
            )
