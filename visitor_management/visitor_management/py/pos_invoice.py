import frappe

def update_cusomer_group(doc,  action):
    if(doc.status=='Paid'):
        cus=frappe.get_doc('Customer', doc.customer)
        prev_grp=cus.customer_group
        reg=frappe.get_single('Registration Settings')
        reg_id=int(cus.registration_id) if(cus.registration_id) else reg.last_registration_id
        next_grp=frappe.get_value('Customer Group', cus.customer_group, 'next_customer_group')
        if(next_grp):
            cus.update({
                'customer_group': next_grp,
            })
            if(not cus.registration_id):
                if(str(reg_id+1) in frappe.get_all('Customer',pluck='registration_id')):
                    frappe.throw(f'Registration ID {reg_id+1} is already taken.')
                reg.update({
                    'last_registration_id': reg_id+1
                })
                if(next_grp):
                    cus.update({
                        'registration_id':str(reg_id+1)
                    })
            cus.save(ignore_permissions=True)
            reg.save(ignore_permissions=True)
            if(prev_grp!=next_grp):
                frappe.msgprint(f'Registration Type {prev_grp} is updated to {next_grp}')
        else:
            frappe.msgprint(f'Next Customer Group is not specified for {cus.customer_group}')