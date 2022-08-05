import frappe

@frappe.whitelist()
def total_fee(evn):
    doc =  frappe.get_doc("Event",evn)
    return doc.registration_fee