# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now_datetime
from frappe.model.document import Document

class ScanQrcode(Document):
	pass

@frappe.whitelist()
def scan_qr_code(data, entry_type='0'):
	if(entry_type and data and entry_type!='0'):
		data=data.split('\n')
		doc=frappe.get_doc('Member Tracking', data[4]+'-'+data[3])
		if(entry_type=='Check In'):
			if(doc.event_checkin==1):
				return {'msg':'Already Checked In', 'colour':'red'}
			doc.update({
				'event_checkin': 1,
				'event_checkin_time': now_datetime()
			})
		if(entry_type=='Check Out'):
			if(doc.event_check_out==1):
				return {'msg':'Already Checked Out', 'colour':'red'}
			doc.update({
				'event_check_out': 1,
				'event_check_out_time': now_datetime()
			})
		if(entry_type=='Dinning Check-in'):
			if(doc.dinning_check_inn==1):
				return {'msg':'Already Checked In for Dinning', 'colour':'red'}
			doc.update({
				'dinning_check_inn': 1,
				'dinning_check_inn_time': now_datetime()
			})
		if(entry_type=='Hall Check-in'):
			if(doc.hall_checkin==1):
				return {'msg':'Already Checked In for Hall', 'colour':'red'}
			doc.update({
				'hall_checkin': 1,
				'hall_checkin_time': now_datetime()
			})
		doc.save(ignore_permissions=True)
		return {'msg': entry_type+' is created successfully', 'colour':'green'}
	else:
		return {'msg':"Couldn't read the data in the Qr Code", 'colour':'red'}