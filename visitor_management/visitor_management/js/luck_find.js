frappe.ui.form.on("Lucky Draw",{
    onload: function(frm, cdt, cdn) {
    var item = locals[cdt][cdn];
    var count = item.count;
    
    frappe.call({
        method: 'visitor_management.visitor_management.py.luc_draw.random_pick',
        args: {count},
        callback(r) {
            

            for(var i=0;i<r.message.length;i++){
                var child = cur_frm.add_child("winners_list1");
                frappe.model.set_value(child.doctype, child.name, "registration_id", r.message[i])
               
            }
       }
    });
    }

} )