# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime
from visitor_management.visitor_management.doctype.member_tracking.member_tracking import create_qr_code

class PDFPrint(Document):
	pass


@frappe.whitelist()
def pdf_print(name, count=1, ts_from=None, entry_type=None):
	if(ts_from=='scan_qr' and entry_type):
		count=int(count)
		if(name and count):
			doc=frappe.get_doc('Member Tracking', name)
			if(entry_type=='Check In'):
				doc.update({
					'event_checkin': 1,
					'event_checkin_time': str(doc.event_checkin_time or "") + "\n" + str(now_datetime()),
					'event_check_inn_count': int(doc.event_check_inn_count or 0) + 1
				})
				length = len((doc.event_checkin_time).split("\n"))
			if(entry_type=='Check Out'):
				doc.update({
					'event_check_out': 1,
					'event_check_out_time': str(doc.event_check_out_time or "") + "\n" + str(now_datetime()),
					'event_check_out_count': int(doc.event_check_out_count or 0) + count
				})
				length = len((doc.event_check_out_time).split("\n"))
			if(entry_type=='Dinning Check-in'):
				doc.update({
					'dinning_check_inn': 1,
					'dinning_check_inn_time': str(doc.dinning_check_inn_time or "") + "\n" + str(now_datetime()),
					'dinning_check_inn_count': int(doc.dinning_check_inn_count or 0) + count
				})
				length = len((doc.dinning_check_inn_time).split("\n"))
			if(entry_type=='Tag Issued'):
				doc.update({
					'print': 1,
					'print_time': str(doc.print_time or "") + "\n" + str(now_datetime()),
					'tag_print_count': int(doc.tag_print_count or 0) + count
				})
				length = len((doc.print_time).split("\n"))
			if(entry_type=='Hall Check-in'):
				doc.update({
					'hall_checkin': 1,
					'hall_checkin_time': str(doc.hall_checkin_time or "") + "\n" + str(now_datetime()),
					'hall_check_inn_count': int(doc.hall_check_inn_count or 0) + count
				})
				length = len((doc.hall_checkin_time).split("\n"))
			if(entry_type=='Open Print'):
				return {'msg':"Checkin is not created", 'colour':'red', 'name': doc.name, 'visitor_count': (doc.count or  1)}
			doc.save(ignore_permissions=True)
			return {'msg': entry_type+f' is created successfully'+(f', Previous {entry_type}: {length-1}' if ((length-1)>1) else "") , 'colour':'green', 'name':doc.name, 'visitor_count':(doc.count or 1)}
	else:
		count=int(count)
		if(name and count):
			doc=frappe.get_doc('Member Tracking', name)
			doc.update({
				'print': 1,
				'print_time': str(doc.print_time or '')+'\n'+str(now_datetime()),
				'tag_print_count': int(doc.tag_print_count or 0) + count
			})
			doc.save()
			length = len((doc.print_time).split("\n"))
		return {'doc': doc, 'msg': 'Tag Issued is created successfully'+(f', Previous Tag Issued: {length-1}' if ((length-1)>1) else "") , 'colour':'green'}