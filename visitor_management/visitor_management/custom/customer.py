import frappe
import re
from frappe.utils import now_datetime

from frappe.exceptions import DuplicateEntryError


def after_save(doc,action):
    
    contact(doc,action)
    address(doc,action)
    member_tracking(doc)


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
    new_contact_doc.save(ignore_permissions=True)

def address(doc,action):
    new_address_doc = frappe.new_doc("Address")
    new_fields = {
            'address_title':doc.organization_name,
            'address_line1':doc.address or doc.organization_name,
            'email_id':doc.email_ids,
            'phone':doc.phone_no,
            'states':doc.state,
            'country':doc.country,
            'district':doc.district,
            'taluk':doc.taluk,
            'whatsapp_number':doc.whatsapp_number
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
    new_address_doc.save(ignore_permissions=True)
def validate_phone(doc,action):
    phone_number(doc,action)
    whatsapp_number(doc,action)

def validate_entry(doc,action=None):
    customer_list = frappe.get_all('Customer',pluck="whatsapp_number")
    if(doc.whatsapp_number in customer_list):
        customer_name = frappe.get_all('Customer',{'whatsapp_number':doc.whatsapp_number},pluck="customer_name")
        if(customer_name[0]!=doc.customer_name):
            member_tracking(doc)
            frappe.msgprint('Successfully registered for the event.')
            frappe.throw(f'Whatsapp Number Already Exist for {customer_name[0]}')
        else:
            member_tracking(doc)
            frappe.msgprint('Successfully registered for the event.')
            raise frappe.exceptions.DuplicateEntryError('Customer name already exist')



def member_tracking(doc):
    if(doc.event):
        customer_name = frappe.get_all('Customer',{'whatsapp_number':doc.whatsapp_number},["customer_name","customer_group"])
        if(doc.event+'-'+doc.whatsapp_number in frappe.get_all('Member Tracking',pluck='name')):
            frappe.throw('Already registered for the event.')
        new = frappe.new_doc("Member Tracking")
        new.update({
            'event_participation' : doc.are_you_attending_event,
            'event': doc.event,
            'mobile_number' : doc.whatsapp_number,
            'customer_group' : customer_name[0]['customer_group'],
            'customer': customer_name[0]['customer_name'],
            'count' : doc.visitor_count,
            
        })
        if(doc.spot_registration==1):
            new.update({
                "spot_registration" : 1,
                "spot_registration_time" : str(now_datetime())
                    })
        else:
            new.update({
                "registration" : 1,
                "registration_time" : str(now_datetime())
            })
        new.save(ignore_permissions=True)
        frappe.db.commit()
    
       


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


