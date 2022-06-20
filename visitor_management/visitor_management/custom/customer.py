import frappe
import re

def after_save(doc,action):
    frappe.set_user('Administrator')
    contact(doc,action)
    address(doc,action)

def contact(doc,action):
         
    new_contact_doc = frappe.new_doc("Contact")
    new_fields = {
                "first_name":doc.customer_name,
                "whatsapp_number":doc.whatsapp_number,
                "is_primary_contact":1,
                'is_billing_contact':1,
    }
    new_contact_doc.update(new_fields)
    if doc.email_ids:
        email_id_table = []
        email_id = {
                        'email_id': doc.email_ids,
                        'is_primary': 1,
        }
        email_id_table.append(email_id)
        new_contact_doc.update({
                'email_ids':email_id_table
        })

    if doc.phone_no:
        phone_no_table=[]
        phone_no={
                        "phone":doc.phone_no,
                        "is_primary_phone":1,
                        "is_primary_mobile_no":1,
        }
        phone_no_table.append(phone_no)
        new_contact_doc.update({
                'phone_nos':phone_no_table
        })
    contact_link_table=[]
    contact_link={
                "link_doctype":'Customer',
                "link_name":doc.customer_name
    }
    contact_link_table.append(contact_link)
    new_contact_doc.update({
                'links':contact_link_table
    })
    new_contact_doc.save()

def address(doc,action):
    new_address_doc = frappe.new_doc("Address")
    new_fields = {
            'address_title':doc.organization_name,
            'address_line1':doc.address,
            'email_id':doc.email_ids,
            'phone':doc.phone_no,
            'states':doc.state,
            'country':doc.country,
            'district':doc.district,
            'taluk':doc.taluk,
    }
    

    new_address_doc.update(new_fields)
    contact_link_table=[]
    contact_link={
            "link_doctype":'Customer',
            "link_name":doc.customer_name
    }
    contact_link_table.append(contact_link)
    new_address_doc.update({
            'links':contact_link_table
    })
    new_address_doc.save()
def validate_phone(doc,action):
    phone_number(doc,action)
    whatsapp_number(doc,action)


def phone_number(doc,action):
   phone_no = doc.phone_no
   if phone_no:
       if not phone_no.isdigit() or len(phone_no) != 10:
           frappe.throw(frappe._("{0} is not a valid Phone Number.").format(phone_no), frappe.InvalidPhoneNumberError)

def whatsapp_number(doc,action):
   whatsapp_number= doc.whatsapp_number
   if whatsapp_number:
       if not whatsapp_number.isdigit() or len(whatsapp_number) != 10:
           frappe.throw(frappe._("{0} is not a valid WhatsApp Number.").format(whatsapp_number), frappe.InvalidPhoneNumberError)


def check(email_ids):
    if(re.fullmatch(regex, email_ids)):
        print("Valid Email")
    else:
        print("Invalid Email")