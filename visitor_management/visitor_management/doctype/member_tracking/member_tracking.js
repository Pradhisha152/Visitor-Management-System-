// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('Member Tracking', {
	refresh: function(frm) {
		frm.set_query('event', function(frm){
			return {
				filters:{
					'status': "Open"
				}
			}
		})
	},
	registration: function(frm){
		if(frm.doc.registration){
			frm.set_value('registration_time', frappe.datetime.now_datetime())
		}
		else{
			frm.set_value('registration_time','')
		}
	},
	event_checkin: function(frm){
		if(frm.doc.event_checkin){
			frm.set_value('event_checkin_time', frappe.datetime.now_datetime())
		}
		else{
			frm.set_value('event_checkin_time','')
		}
	},
	hall_checkin: function(frm){
		if(frm.doc.hall_checkin){
			frm.set_value('hall_checkin_time', frappe.datetime.now_datetime())
		}
		else{
			frm.set_value('hall_checkin_time','')
		}
	},
	dinning_check_inn: function(frm){
		if(frm.doc.dinning_check_inn){
			frm.set_value('dinning_check_inn_time', frappe.datetime.now_datetime())
		}
		else{
			frm.set_value('dinning_check_inn_time','')
		}
	},
	event_check_out: function(frm){
		if(frm.doc.event_check_out){
			frm.set_value('event_check_out_time', frappe.datetime.now_datetime())
		}
		else{
			frm.set_value('event_check_out_time','')
		}
	}
});
