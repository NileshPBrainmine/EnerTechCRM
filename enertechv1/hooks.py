app_name = "enertechv1"
app_title = "EnerTechv1"
app_publisher = "Brainmine AI"
app_description = "Custom App for the EnerTech UPS"
app_email = "nileshp01@brainmine.ai"
app_license = "mit"

# Scheduled Tasks
scheduler_events = {
    "daily": [
        # Lead follow-up reminders
        "enertechv1.lead_utils.followup.notify_client_before_followup",
        # "enertechv1.lead_utils.followup.create_todo_on_followup_date",  # Uncomment if needed
        "enertechv1.lead_utils.followup.create_task_activity_on_followup_date",
        "enertechv1.lead_utils.followup.notify_salesperson_after_due",
        "enertechv1.lead_utils.followup.escalate_to_manager",

        # Quotation follow-up (new)
        "enertechv1.quotation_utils.followup.send_client_followup"
    ],
    "hourly": [
        # Ticket inactivity check (24-hour no-activity notifier)
        "enertechv1.ticket_utils.inactivity_checker.notify_inactive_tickets"
    ]
}

# Doctype Event Hooks
doc_events = {
    "Quotation": {
        "before_submit": "enertechv1.quotation_utils.hooks.set_sent_date"
    },
    "Ticket": {
        "on_update": "enertechv1.ticket_utils.activity_hooks.update_last_activity"
    },
    "Comment": {
        "after_insert": "enertechv1.ticket_utils.activity_hooks.update_last_activity"
    }
}

# Fixtures to export and include with the app
fixtures = [
    {"doctype": "Custom Field", "filters": [["dt", "in", ["Quotation", "Ticket"]]]},
    "Property Setter",
    # "Custom Script",  # Uncomment if needed
    "Workflow",
    "Print Format"
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "enertechv1",
# 		"logo": "/assets/enertechv1/logo.png",
# 		"title": "EnerTechv1",
# 		"route": "/enertechv1",
# 		"has_permission": "enertechv1.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/enertechv1/css/enertechv1.css"
# app_include_js = "/assets/enertechv1/js/enertechv1.js"

# include js, css files in header of web template
# web_include_css = "/assets/enertechv1/css/enertechv1.css"
# web_include_js = "/assets/enertechv1/js/enertechv1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "enertechv1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "enertechv1/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "enertechv1.utils.jinja_methods",
# 	"filters": "enertechv1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "enertechv1.install.before_install"
# after_install = "enertechv1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "enertechv1.uninstall.before_uninstall"
# after_uninstall = "enertechv1.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "enertechv1.utils.before_app_install"
# after_app_install = "enertechv1.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "enertechv1.utils.before_app_uninstall"
# after_app_uninstall = "enertechv1.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "enertechv1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"enertechv1.tasks.all"
# 	],
# 	"daily": [
# 		"enertechv1.tasks.daily"
# 	],
# 	"hourly": [
# 		"enertechv1.tasks.hourly"
# 	],
# 	"weekly": [
# 		"enertechv1.tasks.weekly"
# 	],
# 	"monthly": [
# 		"enertechv1.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "enertechv1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "enertechv1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "enertechv1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["enertechv1.utils.before_request"]
# after_request = ["enertechv1.utils.after_request"]

# Job Events
# ----------
# before_job = ["enertechv1.utils.before_job"]
# after_job = ["enertechv1.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"enertechv1.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

