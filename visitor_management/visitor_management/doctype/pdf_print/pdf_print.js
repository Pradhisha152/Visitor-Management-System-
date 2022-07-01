// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('PDF Print', {
	refresh: function(frm) {
		frm.disable_save()
		frm.add_custom_button('Issue', function(){
			if(frm.doc.mobile_number && frm.doc.visitor_count){
					frappe.call({
						method:"visitor_management.visitor_management.doctype.pdf_print.pdf_print.pdf_print",
						args:{
							name: frm.doc.mobile_number,
							count: frm.doc.count?frm.doc.count:1
						},
						callback: function(r){
							frappe.show_alert({'message': r.message.msg,'indicator': r.message.colour})
							if(frm.doc.go_to_print)
							{
								let res=r.message.doc
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
									frappe.msgprint(__('Please enable pop-ups'));
									return;
								}
							}
						}
					})
			}
			else{
				frappe.show_alert({'message':'Please enter Mobile Number and Visitor Count','indicator':'red'},1.5)
			}
		}).addClass("btn-primary");
	},
	scan_qr: function(frm){
		if(frm.doc.scan_qr){
			let entry_type='Tag Issued'
			if(entry_type){
				frappe.call({
					method: "visitor_management.visitor_management.doctype.scan_qr_code.scan_qr_code.scan_qr_code",
					args:{
						data: frm.doc.scan_qr,
						entry_type: entry_type,
						count: frm.doc.count?frm.doc.count:1
					},
					callback: function(r){
						frm.set_value('scan_qr','')
						frappe.show_alert({'message': r.message.msg,'indicator': r.message.colour})
						if(frm.doc.go_to_print){
							if(r.message.name && r.message.visitor_count){
									frappe.call({
										method:"visitor_management.visitor_management.doctype.pdf_print.pdf_print.pdf_print",
										args:{
											name: r.message.name,
											count: frm.doc.count?frm.doc.count:1
										},
										callback: function(r){
											let res=r.message.doc
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
