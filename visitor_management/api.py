import frappe
from fileinput import filename
from pydoc import doc
from frappe.model import document
from frappe.model.document import Document
import io
import frappe
import os
import http.client
import json
from frappe.utils import get_url
from pyqrcode import create as qr_create

@frappe.whitelist(allow_guest=True)
def get_state(doctype, field):
	value=frappe.db.get_list('State', filters={'country': field},pluck='name')
	return value
@frappe.whitelist(allow_guest=True)
def get_district(doctype, field):
	value=frappe.db.get_list('District', filters={'state': field},pluck='name')
	return value
@frappe.whitelist(allow_guest=True)
def get_taluk(doctype, field):
	value=frappe.db.get_list('Taluk', filters={'district': field},pluck='name')
	return value

class Visitor(Document ):
    def on_submit(self):
        data = "Name :"+self.name1+"\n"+"Mobile Number :"+self.mobile_number+"\n"+"Territory :"+self.taluk_
        file = create_qr_code(data)
        
        send_invoice(self.mobile_number,file.file_url,file.file_name)

@frappe.whitelist()
def create_qr_code(data):
    qr_image = io.BytesIO()
    data_ = qr_create(data, error='L')
    data_.png(qr_image, scale=4, quiet_zone=1)
    name = frappe.generate_hash('', 5)
    filename = f"QRCode-{name}.pdf".replace(os.path.sep, "__")
    _file = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "is_private": 0,
        "content": qr_image.getvalue()
    })
    _file.save()
    frappe.db.commit()

	
@frappe.whitelist()
def send_invoice(mobile_no, link,filename):
  if(link):
    # link=frappe.utils.get_url()+link
    print("----------------------")
    # print(link),
    print("****************************")
    conn = http.client.HTTPSConnection("api.interakt.ai")
    payload = json.dumps({
    "countryCode": "+91",
    "phoneNumber": mobile_no,
    "callbackData": "some text here",
    "type": "Template",
    "template": {
      "name": "test",
      "languageCode": "en",
      "headerValues": [ link ],
      "fileName": filename,
      "bodyValues": [
        "body_variable_value"
      ]
    }
  })
    headers = {
    'Authorization': "Basic eHd0aHJaNUp6NjFvZF9qTFYwaml2YV9uSGdIbVR5ZFpad1JtYkREeng5czo=",
    'Content-Type': 'application/json',
    'Cookie': 'ApplicationGatewayAffinity=a8f6ae06c0b3046487ae2c0ab287e175; ApplicationGatewayAffinityCORS=a8f6ae06c0b3046487ae2c0ab287e175'
  }
    conn.request("POST", "/v1/public/message/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    # print("----------------------------")
    print(data)
    # print("////////////////////////////////////")