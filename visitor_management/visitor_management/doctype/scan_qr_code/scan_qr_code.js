// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('Scan Qr code', {
	refresh: function(frm) {
		frm.disable_save()
		cur_frm.fields_dict.checkin.$input.on("click", function() {
			frm.set_value('checkout', 0)
			frm.set_value('dinningin', 0)
			frm.set_value('hall_check_in', 0)
		})
		cur_frm.fields_dict.checkout.$input.on("click", function() {
			frm.set_value('checkin', 0)
			frm.set_value('dinningin', 0)
			frm.set_value('hall_check_in', 0)
		})
		cur_frm.fields_dict.dinningin.$input.on("click", function() {
			frm.set_value('checkout', 0)
			frm.set_value('checkin', 0)
			frm.set_value('hall_check_in', 0)
		})
		cur_frm.fields_dict.hall_check_in.$input.on("click", function() {
			frm.set_value('checkout', 0)
			frm.set_value('checkin', 0)
			frm.set_value('dinningin', 0)
		})
	},
	scan_qr: function(frm){
		if(frm.doc.scan_qr){
			let checkin=frm.doc.checkin
			let checkout=frm.doc.checkout
			let dinningin=frm.doc.dinningin
			let hallcheckin=frm.doc.hall_check_in
			let open_print=frm.doc.open_print_after_scan
			let entry_type=checkin?'Check In':(checkout?'Check Out':(dinningin?'Dinning Check-in':(hallcheckin?'Hall Check-in':(open_print?'Open Print':0))))
			if(entry_type){
				frappe.call({
					method: "visitor_management.visitor_management.doctype.scan_qr_code.scan_qr_code.scan_qr_code",
					args:{
						data: frm.doc.scan_qr,
						entry_type: entry_type
					},
					callback: function(r){
						frm.set_value('scan_qr','')
						frappe.show_alert({'message': r.message.msg,'indicator': r.message.colour})
						if(frm.doc.open_print_after_scan){
							if(r.message.name && r.message.visitor_count){
									frappe.call({
										method:"visitor_management.visitor_management.doctype.pdf_print.pdf_print.pdf_print",
										args:{
											name: r.message.name,
											count: r.message.visitor_count
										},
										callback: function(r){
											let res=r.message
											let url=frappe.urllib.get_full_url(
												'/api/method/frappe.utils.print_format.download_pdf?' +
													'doctype=' +
													encodeURIComponent(res.doctype) +
													'&name=' +
													encodeURIComponent(res.name) +
													'&trigger_print=1' +
													'&format=' +
													encodeURIComponent('TRMAO') +
													'&no_letterhead=' + '1' +
													'&letterhead=' +
													encodeURIComponent("TRMOA") 
											)							
											let w = window.open(url);
											if (!w) {
												frappe.show_alert({'message': 'Please enable pop-ups in your browser','indicator': 'red'});
												return;
											}
										}
									})
							}
							
						}
					}
				})
			}
			else{
				frm.set_value('scan_qr','')
				frappe.show_alert({'message': 'Please choose entry type!','indicator': 'red'})
			}
		}
	}
});
