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
		if(len(data)<5):
			return {'msg':"Couldn't read the data in the Qr Code", 'colour':'red', 'name':'', 'visitor_count':''}
		name = data[4]+'-'+data[3]
		length = 0
		if(name not in frappe.get_all('Member Tracking',pluck='name')):
			return {'msg':"Couldn't read the data in the Qr Code", 'colour':'red'}
		doc=frappe.get_doc('Member Tracking', name)
		if(entry_type=='Check In'):
			doc.update({
				'event_checkin': 1,
				'event_checkin_time': str(doc.event_checkin_time or "") + "\n" + str(now_datetime())
			})
			length = len((doc.event_checkin_time).split("\n"))
		if(entry_type=='Check Out'):
			doc.update({
				'event_check_out': 1,
				'event_check_out_time': str(doc.event_check_out_time or "") + "\n" + str(now_datetime())
			})
			length = len((doc.event_check_out_time).split("\n"))
		if(entry_type=='Dinning Check-in'):
			doc.update({
				'dinning_check_inn': 1,
				'dinning_check_inn_time': str(doc.dinning_check_inn_time or "") + "\n" + str(now_datetime())
			})
			length = len((doc.dinning_check_inn_time).split("\n"))
		if(entry_type=='Hall Check-in'):
			doc.update({
				'hall_checkin': 1,
				'hall_checkin_time': str(doc.hall_checkin_time or "") + "\n" + str(now_datetime())
			})
			length = len((doc.hall_checkin_time).split("\n"))
		if(entry_type=='Open Print'):
			return {'msg':"Checkin is not created", 'colour':'red', 'name': doc.name, 'visitor_count': (doc.count or  1)}
		doc.save(ignore_permissions=True)
		return {'msg': entry_type+f' is created successfully'+(f', Previous {entry_type}: {length-1}' if ((length-1)>1) else "") , 'colour':'green', 'name':doc.name, 'visitor_count':(doc.count or 1)}
	else:
		return {'msg':"Couldn't read the data in the Qr Code", 'colour':'red', 'name':'', 'visitor_count':''}