from __future__ import unicode_literals

import frappe

def get_context(context):
	# do your magic here
	pass


def send_invoice(cus, name, doctype):

  link=frappe.get_value(doctype, name, 'print_link') or None
  if(link):
    link=frappe.utils.get_url()+link
    mb=frappe.get_doc("Contact",cus+'-'+cus)
    conn = http.client.HTTPSConnection("api.interakt.ai")
    payload = json.dumps({
    "countryCode": "+91",
    "phoneNumber": mb.mobile_no,
    "callbackData": "some text here",
    "type": "Template",
    "template": {
      "name": "test",
      "languageCode": "en",
      "headerValues": [ link ],
      "fileName": "SINV-22-00008.pdf",
      "bodyValues": [
        "Mani"
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
    print(data.decode("utf-8"))