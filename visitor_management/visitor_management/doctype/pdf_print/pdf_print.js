// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('PDF Print', {
	refresh: function(frm) {
		frm.disable_save()
		frm.add_custom_button('Print', function(){
			if(frm.doc.mobile_number && frm.doc.visitor_count){
					frappe.call({
						method:"visitor_management.visitor_management.doctype.pdf_print.pdf_print.pdf_print",
						args:{
							name: frm.doc.mobile_number,
							count: frm.doc.visitor_count
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
								frappe.msgprint(__('Please enable pop-ups'));
								return;
							}
						}
					})
			}
			else{
				frappe.show_alert({'message':'Please enter Mobile Number and Visitor Count','indicator':'red'},1.5)
			}
		}).addClass("btn-primary");
	}
});
