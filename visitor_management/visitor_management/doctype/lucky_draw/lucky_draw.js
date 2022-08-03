frappe.ui.form.on("Lucky Draw",{
    winners_button: function(frm, cdt, cdn) {
    var docu = locals[cdt][cdn];
    var count = docu.count; 
	var event_name = docu.event_name
    var winn_list = docu.winners_list1
    if (winn_list.length!=0) {
        count=count-winn_list.length;
    }
   
    frappe.call({
        method:"visitor_management.visitor_management.doctype.lucky_draw.lucky_draw.random_pick",
        freeze :true,
        freeze_message: 'Fetching Winners List',

        args: {cnt:count, evn:event_name },
        callback(r) {
            for(var i=0;i<r.message.length;i++){
                var child = cur_frm.add_child("winners_list1");
                frappe.model.set_value(child.doctype, child.name, "registration_id", r.message[i]) 
            }
			frm.refresh_field('winners_list1')
       }
    });
    }

} )

frappe.ui.form.on("Lucky Draw",{
    onload:function(frm){
        if (frm.doc.__islocal || frm.doc.docstatus== 1 ) {
            frm.set_df_property("winners_button","hidden",1);
        }
    }
})

frappe.ui.form.on("Lucky Draw",{
    after_save:function(frm){
        
          
        if (frm.doc.docstatus== 0) {
            frm.set_df_property("winners_button","hidden",0);
        }
        
        else {
            frm.set_df_property("winners_button","hidden",1);
        }
    }
})