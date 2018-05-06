# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "accurate_erp"
app_title = "Accurate Erp"
app_publisher = "mohammed redah"
app_description = "home page for accurate system company"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "mhbu50@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accurate_erp/css/accurate_erp.css"
# app_include_js = "/assets/accurate_erp/js/accurate_erp.js"

# include js, css files in header of web template
# web_include_css = "/assets/accurate_erp/css/accurate_erp.css"
# web_include_js = "/assets/accurate_erp/js/accurate_erp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }
role_home_page = {
		"Guest": "index-ar"
}

# Website user home page (by function)
# get_website_user_home_page = "accurate_erp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "accurate_erp.install.before_install"
# after_install = "accurate_erp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accurate_erp.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accurate_erp.tasks.all"
# 	],
# 	"daily": [
# 		"accurate_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"accurate_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accurate_erp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"accurate_erp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "accurate_erp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accurate_erp.event.get_events"
# }

