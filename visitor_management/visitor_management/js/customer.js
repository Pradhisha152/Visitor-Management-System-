frappe.ui.form.on("Customer", {
    refresh: function(frm) {
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
    }
})