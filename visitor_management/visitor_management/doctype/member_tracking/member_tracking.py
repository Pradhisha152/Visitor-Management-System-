# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import io
import os
import http.client
import json
from pyqrcode import create as qr_create
from frappe.utils.pdf import get_pdf

class MemberTracking(Document):
	def after_insert(self):
		customer_group=frappe.get_all('Customer', {'whatsapp_number': self.mobile_number}, pluck="customer_group")
		org_name=frappe.get_value('Customer', self.customer, 'organization_name') or ''
		data = (self.customer or '')+"\n"+(customer_group[0] if(customer_group) else '')+"\n"+org_name+"\n"+(self.mobile_number or '')+"\n"+(self.event or '')+"\n"+(self.taluk or '')
		qr_url = create_qr_code(self, data)
		frappe.db.set_value(self.doctype, self.name, 'qr_url', qr_url)
		frappe.db.commit()
		path='visitor_management/visitor_management/doctype/member_tracking/membertrack.html'
		html=frappe.render_template(path, {'doc': frappe.get_doc('Member Tracking', self.name)})
		file = frappe.get_doc({
		"doctype": "File",
		"file_name": f"{self.name}.pdf",
		"is_private": 0,
		"content": get_pdf(html),
		"attached_to_doctype":  self.doctype,
		"attached_to_name": self.name
	    }) 
		file.save(ignore_permissions=True)
		send_invitation(self.mobile_number, self.event, self.customer)
		send_invoice(self.mobile_number,file.file_url,file.file_name, self.customer)

@frappe.whitelist()
def create_qr_code(self, data):
	qr_image = io.BytesIO()
	data_ = qr_create(data, error='L')
	data_.png(qr_image, scale=4, quiet_zone=1)
	name = frappe.generate_hash('', 5)
	filename = f"QRCode-{name}.png".replace(os.path.sep, "__")
	_file = frappe.get_doc({
		"doctype": "File",
		"file_name": filename,
		"is_private": 0,
		"content": qr_image.getvalue(),
		"attached_to_doctype":  self.doctype,
		"attached_to_name": self.name
	})
	_file.save(ignore_permissions=True)
	return _file.file_url

@frappe.whitelist()
def send_invoice(mobile_no, link,filename, cus_name):
	if(link):
		link=frappe.utils.get_url()+link
		conn = http.client.HTTPSConnection("api.interakt.ai")
		payload = json.dumps({
		"countryCode": "+91",
		"phoneNumber": mobile_no,
		"callbackData": "some text here",
		"type": "Template",
		"template": {
		"name": "registration_confirmation",
		"languageCode": "en",
		"headerValues": [ link ],
		"fileName": filename,
		"bodyValues": [
			cus_name
		]
		}
	})
		headers = {
		'Authorization': "Basic eHd0aHJaNUp6NjFvZF9qTFYwaml2YV9uSGdIbVR5ZFpad1JtYkREeng5czo=",
		'Content-Type': 'application/json',
		'Cookie': 'ApplicationGatewayAffinity=a8f6ae06c0b3046487ae2c0ab287e175; ApplicationGatewayAffinityCORS=a8f6ae06c0b3046487ae2c0ab287e175'
	}
		conn.request("POST", "/v1/public/message/", payload, headers)
		res = conn.getresponse()
		data = res.read()
		
def send_invitation(mobile_no, event,cus_name):
	for url in frappe.get_all('Event Messages', {'parent':event, 'send_this_document':1, 'file_attachment':['!=', '']}, pluck="file_attachment"):
		link=url
		if(link):
			link='https://trmoa.thirvusoft.com'+link
			conn = http.client.HTTPSConnection("api.interakt.ai")
			payload = json.dumps({
			"countryCode": "+91",
			"phoneNumber": mobile_no,
			"callbackData": "some text here",
			"type": "Template",
			"template": {
			"name": "registration_confirmation",
			"languageCode": "en",
			"headerValues": [ link ],
			"fileName": "Invitation.pdf",
			"bodyValues": [
				cus_name
			]
			}
		})
			headers = {
			'Authorization': "Basic eHd0aHJaNUp6NjFvZF9qTFYwaml2YV9uSGdIbVR5ZFpad1JtYkREeng5czo=",
			'Content-Type': 'application/json',
			'Cookie': 'ApplicationGatewayAffinity=a8f6ae06c0b3046487ae2c0ab287e175; ApplicationGatewayAffinityCORS=a8f6ae06c0b3046487ae2c0ab287e175'
		}
			conn.request("POST", "/v1/public/message/", payload, headers)
			res = conn.getresponse()
			data = res.read()
		
