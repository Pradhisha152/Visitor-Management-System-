# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class RegistrationForm(Document):
	pass
import frappe

@frappe.whitelist()
def event_fee(cnt,evn):
	fee_per_head =  frappe.db.get_value("Event",evn,"registration_fee")
	total = cnt *int(fee_per_head)
	print(total)
	return total