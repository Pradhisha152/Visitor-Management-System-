# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters={}):
	columns, data = [], []
	columns =get_columns(filters)
	data =get_data(filters)
	return columns, data

def get_columns(filters):
	columns=[
		{
			"label":_("Whatsapp No"),
			"fieldtype":"Data",
			"fileldname":"mobile_number",
			"width":150
		},
		{
			"label":_("Participants"),
			"fieldtype":"Data",
			"fileldname":"customer",
			"width":150
		}
	]
	if filters.get('report')=='Tag Issue':
		columns.append(
			{
			"label":_("Tag Issue Count"),
			"fieldtype":"Int",
			"fileldname":"tag_print_count",
			"width":150
			}
		)
	if filters.get('report')=='Event check inn':
		columns.append(
			{
			"label":_("Event check inn count"),
			"fieldtype":"Int",
			"fileldname":"event_check_inn_count",
			"width":150
			}
		)
	if filters.get('report')=='Hall check inn':
		columns.append(
			{
			"label":_("Hallcheck inn count"),
			"fieldtype":"Int",
			"fileldname":"hall_check_inn_count",
			"width":150
			}
		)
	if filters.get('report')=='Dinning check inn':
		columns.append(
			{
			"label":_("Dinning inn count"),
			"fieldtype":"Int",
			"fileldname":"dinning_check_inn_count",
			"width":150
			}
		)
	if filters.get('report')=='Event check out':
		columns.append(
			{
			"label":_("Event check out Count"),
			"fieldtype":"Int",
			"fileldname":"event_check_out_count",
			"width":150
			}
		)
	return columns

def get_data(filters):
	ts_filters={}
	ts_fields=['customer', 'mobile_number']
	if filters.get('report')=='Registration':
		ts_filters={'registration':1}

	if filters.get('report')=='Spot Registration':
		ts_filters={'spot_registration':1}

	if filters.get('report')=='Tag Issue':
		ts_filters={'print':1}
		ts_fields.append("tag_print_count")
	
	if filters.get('report')=='Event check inn':
		ts_filters={'event_checkin':1}
		ts_fields.append("event_check_inn_count")

	if filters.get('report')=='Hall check inn':
		ts_filters={'hall_checkin'}
		ts_fields.append('hall_check_inn_count')
	
	if filters.get('report')=='Dinning check inn':
		ts_filters={'dinning_check_inn':1}
		ts_fields.append('dinning_check_inn_count')

	if filters.get('report')=='Event check out':
		ts_filters={'event_check_out':1}
		ts_fields.append('event_check_out_count')


	data=frappe.get_all('Member Tracking', ts_filters, ts_fields)
	data=[list(i.values()) for i in data]
	frappe.errprint(data)
	return data