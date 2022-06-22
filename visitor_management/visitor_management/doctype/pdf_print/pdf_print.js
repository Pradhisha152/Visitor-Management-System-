// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('PDF Print', {
	refresh: function(frm) {
		frm.disable_save()
		frm.add_custom_button('Get PDF', function(){
			if(frm.doc.mobile_number && frm.doc.visitor_count){
					frappe.call({
						method:"visitor_management.visitor_management.doctype.pdf_print.pdf_print.pdf_print",
						args:{
							name: frm.doc.mobile_number,
							count: frm.doc.visitor_count
						},
						callback: function(r){
							let res=r.message
							let w = window.open(
								frappe.urllib.get_full_url(
									method +
										'doctype=' +
										encodeURIComponent(res.doctype) +
										'&name=' +
										encodeURIComponent(res.name) +
										(printit ? '&trigger_print=1' : '') +
										'&format=' +
										encodeURIComponent('') +
										'&no_letterhead=' + '1' +
										'&letterhead=' +
										encodeURIComponent("TRMOA") 
								)
							);
							if (!w) {
								frappe.msgprint(__('Please enable pop-ups'));
								return;
							}
						}
					})
			}
			else{
				frappe.show_alert({'message':'Please enter Mobile Number and Visitor Count','indicator':'red'},1.5)
			}
		})
	}
});
