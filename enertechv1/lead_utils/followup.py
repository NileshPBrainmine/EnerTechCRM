import frappe
from frappe.utils import nowdate, add_days

# 1. Email the client 1 day before follow-up date
def notify_client_before_followup():
    leads = frappe.get_all("Lead",
        filters={
            "follow_up_date": add_days(nowdate(), 1),
            "status": ["not in", ["Converted", "Closed"]]
        },
        fields=["name", "lead_name", "email_id"]
    )

    for lead in leads:
        if lead.email_id:
            frappe.sendmail(
                recipients=[lead.email_id],
                subject="Upcoming Follow-Up",
                message=f"Hi! Just a reminder, we’ll be following up with you regarding <b>{lead.lead_name}</b> tomorrow."
            )

# 2. Create ToDo on follow-up date if no previous ToDo exists
def create_task_activity_on_followup_date():
    from frappe.utils import nowdate

    leads = frappe.get_all("Lead",
        filters={
            "follow_up_date": nowdate(),
            "status": ["not in", ["Converted", "Closed"]]
        },
        fields=["name", "lead_name", "owner"]
    )

    for lead in leads:
        print(f"Checking lead: {lead.name}")

        # Check if a task already exists to avoid duplication
        if frappe.db.exists("ToDo", {
            "reference_type": "Lead",
            "reference_name": lead.name,
            "description": ["like", "%Follow up on lead%"]
        }):
            continue

        # Create a ToDo (shows as Task in Activity tab)
        frappe.get_doc({
            "doctype": "ToDo",
            "description": f"📌 Follow up on lead: {lead.lead_name}",
            "reference_type": "Lead",
            "reference_name": lead.name,
            "owner": lead.owner,
            "date": nowdate(),
            "status": "Open",
            "priority": "Medium"
        }).insert(ignore_permissions=True)



# def create_lead_note_on_followup_date():
#     from frappe.utils import nowdate

#     leads = frappe.get_all("Lead",
#         filters={
#             "follow_up_date": nowdate(),
#             "status": ["not in", ["Converted", "Closed"]]
#         },
#         fields=["name", "lead_name", "owner"]
#     )

#     for lead in leads:
#         print(f"Adding note to lead: {lead.name}")

#         # Add a Comment to the Lead (shows in timeline)
#         frappe.get_doc({
#             "doctype": "Comment",
#             "comment_type": "Comment",
#             "reference_doctype": "Lead",
#             "reference_name": lead.name,
#             "content": f" Reminder: Today is the follow-up date for this lead ({lead.lead_name}). Please take action."
#         }).insert(ignore_permissions=True)



# def create_todo_on_followup_date():
#     leads = frappe.get_all("Lead",
#         filters={
#             "follow_up_date": nowdate(),
#             "status": ["not in", ["Converted", "Closed"]]
#         },
#         fields=["name", "lead_name", "owner"]
#     )

#     for lead in leads:
#         # Avoid duplicate ToDos
#         if not frappe.db.exists("ToDo", {"reference_type": "Lead", "reference_name": lead.name}):
#             frappe.get_doc({
#                 "doctype": "ToDo",
#                 "description": f"Follow up on lead: {lead.lead_name}",
#                 "reference_type": "Lead",
#                 "reference_name": lead.name,
#                 "owner": lead.owner,
#                 "date": nowdate()
#             }).insert(ignore_permissions=True)

# 3. Email the salesperson 1 day after follow-up if no update
def notify_salesperson_after_due():
    leads = frappe.get_all("Lead",
        filters={
            "follow_up_date": add_days(nowdate(), -1),
            "status": ["not in", ["Converted", "Closed", "Pending Follow-Up"]]
        },
        fields=["name", "lead_name", "owner"]
    )

    for lead in leads:
        if lead.owner:
            frappe.sendmail(
                recipients=[lead.owner],
                subject="Follow-Up Not Done",
                message=f"You missed following up on lead: <b>{lead.lead_name}</b> yesterday. Please take action."
            )

# 4. Email the manager if 3+ days have passed without action
def escalate_to_manager():
    leads = frappe.get_all("Lead",
        filters={
            "follow_up_date": ["<", add_days(nowdate(), -3)],
            "status": ["not in", ["Converted", "Closed", "Pending Follow-Up"]]
        },
        fields=["name", "lead_name", "country", "owner"]
    )

    for lead in leads:
        # Replace this with the actual manager's email or fetch from settings
        manager_email = "manager@example.com"

        # Email the manager
        frappe.sendmail(
            recipients=[manager_email],
            subject="Lead Escalation: No Action Taken",
            message=f"""
            <p>Dear Manager,</p>
            <p>The assigned salesperson has not followed up on the lead: <b>{lead.lead_name}</b> for over 3 days.</p>
            <p>Country: <b>{lead.country or 'N/A'}</b></p>
            <p>Please check with the salesperson: <b>{lead.owner}</b>.</p>
            <br>
            <p>Regards,<br>CRM System</p>
            """
        )

        # Optionally update the status
        frappe.db.set_value("Lead", lead.name, "status", "Pending Follow-Up")




























# import frappe
# from frappe.utils import nowdate, add_days

# def send_follow_up_reminders():
#     leads = frappe.get_all("Lead", 
#         filters={
#             "follow_up_date": nowdate(),
#             "status": ["!=", "Converted"]
#         },
#         fields=["name", "lead_name", "email_id", "owner"]
#     )

#     for lead in leads:
#         # 1. Send Email Reminder
#         if lead.email_id:
#             frappe.sendmail(
#                 recipients=[lead.email_id],
#                 subject="Reminder: Follow up on lead",
#                 message=f"Reminder to follow up with lead: {lead.lead_name}"
#             )

#         # 2. Create a ToDo Task
#         frappe.get_doc({
#             "doctype": "ToDo",
#             "description": f"Follow up with lead: {lead.lead_name}",
#             "reference_type": "Lead",
#             "reference_name": lead.name,
#             "owner": lead.owner,
#             "date": nowdate()
#         }).insert(ignore_permissions=True)

# def mark_pending_followup():
#     leads = frappe.get_all("Lead",
#         filters={
#             "follow_up_date": ["<", add_days(nowdate(), -3)],
#             "status": ["not in", ["Converted", "Pending Follow-Up"]]
#         },
#         fields=["name", "lead_name", "country", "owner"]
#     )

#     for lead in leads:
#         # 1. Mark lead as "Pending Follow-Up"
#         frappe.db.set_value("Lead", lead.name, "status", "Pending Follow-Up")

#         # 2. Send email to salesperson
#         if lead.owner:
#             subject = "Your Follow-Up is Pending"
#             message = f"""
#             <p>Dear Salesperson,</p>
#             <p>You have a pending follow-up for the lead: <b>{lead.lead_name}</b></p>
#             <p>Country: <b>{lead.country or 'N/A'}</b></p>
#             <p>This follow-up was due more than 3 days ago. Please take action immediately.</p>
#             <br>
#             <p>Regards,<br>Your CRM System</p>
#             """
#             frappe.sendmail(
#                 recipients=[lead.owner],
#                 subject=subject,
#                 message=message
#             )
