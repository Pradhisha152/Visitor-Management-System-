var ts_frm;
frappe.ui.form.on("Customer", {
    refresh: function(frm) {
		ts_frm=frm.is_new()
		if(frm.is_new()){
			frm.set_value("spot_registration",1)
		}
		frm.set_query("state", function() {
			return {
				"filters": {
					"country" : frm.doc.country
                    
				}
			};
		});
		frm.set_query("district", function() {
			return {
				"filters": {
					"state" : frm.doc.state
                    
				}
			};
		});
		frm.set_query("taluk", function() {
			return {
				"filters": {
					"district" : frm.doc.district
                    
				}
			};
		});
		frm.set_query('customer_group', function(frm){
            return {
                filters: {
                    'next_customer_group': ['!=', '']
                }
            }
        });
    },
	whatsapp_number: function(frm){
		check_number(frm)
	},
	event: function(frm){
		check_number(frm)
	},
	validate: function(frm){
		
		if(frm.is_new()){
			frappe.call({
				method: "visitor_management.visitor_management.custom.customer.duplicate_entry",
				args: {
					whatsapp_number: frm.doc.whatsapp_number?frm.doc.whatsapp_number:''
				},
				callback: function(r){
					let res=r.message
					if(res['error']==1){
						frappe.show_alert({message:'Successfully registered for the event.',indicator:'green'})
						throw new Error('Exception message').then(() =>{
							frappe.new_doc('Customer')
						})
					}
				}
			})
		}
	},
	after_save: function(frm){
		if(ts_frm){
			frappe.show_alert({message:'Successfully registered for the event.',indicator:'green'})
			frappe.new_doc('Customer')
		}
	}
})

function check_number(frm){
	frappe.call({
		method: "visitor_management.visitor_management.custom.customer.check_duplicate",
		args:{
			number:frm.doc.whatsapp_number?frm.doc.whatsapp_number:'',
			event:frm.doc.event?frm.doc.event:''
		},
		callback: function(r){
			let res=r.message
			if(res.duplicate==1){
				frappe.show_alert({message:res.msg,indicator:res.indicator})
				cur_frm.disable_save()
			}
			else{
				cur_frm.enable_save()
			}
		}
	})
}