import frappe

def update_cusomer_group(doc,  action):
    if(doc.status=='Paid'):
        cus=frappe.get_doc('Customer', doc.customer)
        prev_grp=cus.customer_group
        next_grp=frappe.get_value('Customer Group', cus.customer_group, 'next_customer_group')
        if(next_grp):
            cus.update({
                'customer_group': next_grp
            })
            cus.save(ignore_permissions=True)
            if(prev_grp!=next_grp):
                frappe.msgprint(f'Registration Type {prev_grp} is updated to {next_grp}')
        else:
            frappe.msgprint(f'Next Customer Group is not specified for {cus.customer_group}')