// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Event Report"] = {
	"filters": [
		{
			"fieldname":"report",
			"lable":__("Report"),
			"fieldtype":"Select",
			"options":"\nRegistration\nSpot Registration\nTag Issue\nEvent check inn\nHall check inn\nDinning check inn\nEvent check out",
			"reqd":1
		}
	]
};
