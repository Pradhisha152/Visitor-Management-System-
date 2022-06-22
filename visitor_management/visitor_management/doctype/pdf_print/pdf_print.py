# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
from frappe.utils.pdf import get_pdf
from visitor_management.visitor_management.doctype.member_tracking.member_tracking import create_qr_code
from visitor_management.visitor_management.doctype.member_tracking.member_tracking import create_qr_code

class PDFPrint(Document):
	pass


@frappe.whitelist()
def pdf_print(name, count=1):
	count=int(count)
	if(name and count):
		doc=frappe.get_doc('Member Tracking')
		doc.update({
			'count': count,
			'print': 1,
			'print_time': datetime.datetime.now()
		})
		doc.save()
	customer_group=frappe.get_all('Customer', {'whatsapp_number': doc.mobile_number}, pluck="customer_group")
	data = "Name :"+doc.customer+"\n"+"Registration Type :"+(customer_group[0] if(customer_group) else '')+"\n"+"Mobile Number :"+doc.mobile_number+"\n"+"Territory :"+(doc.taluk or '')
	
	qr_url = create_qr_code(doc, data)
	path='visitor_management/visitor_management/doctype/member_tracking/membertrack.html'
	html=frappe.render_template(path, {'doc': doc,'qr_url':qr_url, 'letter_head': 'TRMOA'})
	frappe.local.response.filename = "{name}.pdf".format(
		name=name.replace(" ", "-").replace("/", "-")
	)
	frappe.local.response.filecontent = get_pdf(html)
	frappe.local.response.type = "pdf"