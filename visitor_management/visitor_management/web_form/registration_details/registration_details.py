from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	pass



@frappe.whitelist()
def event_fee(cnt,evn):
	fee_per_head =  frappe.db.get_value("Event",evn,"registration_fee")
	total = cnt *fee_per_head
	
	return total
