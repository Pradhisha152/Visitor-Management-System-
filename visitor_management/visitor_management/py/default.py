import frappe
import erpnext
from frappe import _

def validate_phone(doc,action):
    
    if doc.mob_num:
        if not doc.mob_num.isdigit() or len(doc.mob_num) != 10:
            frappe.throw(frappe._("{0} is not a Valid Mobile Number").format(doc.mob_num),frappe.InvalidPhoneNumberError)