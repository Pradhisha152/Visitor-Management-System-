// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt

frappe.ui.form.on('Registration Form', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on("Registration Form",{
    no_of_participants: function(frm , cdt, cdn) {
    var docu = locals[cdt][cdn];
    var count = docu.no_of_participants
	var event_name = docu.event
	var name = docu.name
    
    console.log("00000000000")
    frappe.call({
        method:"visitor_management.visitor_management.doctype.registration_form.registration_form.event_fee",

        args: {cnt:count, evn:event_name },
        callback(r) {
          
		   frm.set_value('registration_fee',r.message)
       }
    });
    }

} )