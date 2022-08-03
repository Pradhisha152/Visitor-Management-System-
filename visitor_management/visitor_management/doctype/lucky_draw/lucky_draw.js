frappe.ui.form.on("Lucky Draw",{
    validate: function(frm, cdt, cdn) {
    var item = locals[cdt][cdn];
    var count = item.count;
	var event_name = item.event_name
    console.log('ooo')
    frappe.call({
        method:"visitor_management.visitor_management.doctype.lucky_draw.lucky_draw.random_pick",
        args: {cnt:count, evn:event_name },
        
       
        callback(r) {
            
			frm.set_value('winners_list1',[])

            for(var i=0;i<r.message.length;i++){
			
                var child = cur_frm.add_child("winners_list1");
                frappe.model.set_value(child.doctype, child.name, "registration_id", r.message[i])
               
            }
			frm.refresh_field('winners_list1')
       }
    });
    }

} )