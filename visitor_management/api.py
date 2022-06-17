import frappe
@frappe.whitelist(allow_guest=True)
def get_state(doctype, field):
	value=frappe.db.get_list('State', filters={'country': field},pluck='name')
	return value
@frappe.whitelist(allow_guest=True)
def get_district(doctype, field):
	value=frappe.db.get_list('District', filters={'state': field},pluck='name')
	return value
@frappe.whitelist(allow_guest=True)
def get_taluk(doctype, field):
	value=frappe.db.get_list('Taluk', filters={'district': field},pluck='name')
	return value
