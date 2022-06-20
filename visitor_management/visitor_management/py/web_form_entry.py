import frappe

@frappe.whitelist()
def create_entry(qr_details, entry_type='0'):
    if(entry_type=='0'):
        return {'msg':'Please choose Entry Type','colour':'red'}
    doc=frappe.new_doc('TS Entry Details')
    doc.update({
        'visitor_name':'',
        'mobile_no':'',
        'entry_type':entry_type,
        'event':''
    })
    doc.insert()
    doc.submit()
    return {'msg':'Enrty Created Successfully','colour':'green'}
