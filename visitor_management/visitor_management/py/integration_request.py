
import frappe
import json

def validate(doc,event):
    var= doc.status
    var2 = doc.data
    
    var3 = json.loads(var2)
    reg_form = var3["order_id"]
    sales_inv=  frappe.new_doc("Sales Invoice")
    reg = frappe.get_doc("Registration Form",reg_form)
    # sales_inv.customer = reg.name1
    even = frappe.db.get_value("Event",reg.event,"item_event")
    sales_inv.item_code = even
    # sales_inv.qty = 1
    # sales_inv.rate= 100
    # sales_inv.due_date = "05-08-2022"
    sales_inv.save()
  



 