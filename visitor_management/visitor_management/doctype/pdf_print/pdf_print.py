# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
from visitor_management.visitor_management.doctype.member_tracking.member_tracking import create_qr_code

class PDFPrint(Document):
	pass


@frappe.whitelist()
def pdf_print(name, count=1):
	count=int(count)
	if(name and count):
		doc=frappe.get_doc('Member Tracking', name)
		doc.update({
			'count': count,
			'print': 1,
			'print_time': str(doc.print_time or '')+'\n'+str(now_datetime())
		})
		doc.save()
	return doc