frappe.ui.form.on("Customer", {
    refresh: function(frm) {
		frm.set_value("spot_registration",1)
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
    }
})