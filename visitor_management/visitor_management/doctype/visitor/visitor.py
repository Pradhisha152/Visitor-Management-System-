# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt

# import frappe
from pydoc import doc
from frappe.model import document
from frappe.model.document import Document
import io
import frappe
import os
from frappe.utils import get_url
from pyqrcode import create as qr_create

class Visitor(Document):
	def on_submit(self):
		data = "Name :"+self.name1+"\n"+"Mobile Number :"+self.mobile_number+"\n"+"Territory :"+self.taluk
		create_qr_code(data)

@frappe.whitelist()
def create_qr_code(data):
    qr_image = io.BytesIO()
    data_ = qr_create(data, error='L')
    data_.png(qr_image, scale=4, quiet_zone=1)
    name = frappe.generate_hash('', 5)
    filename = f"QRCode-{name}.png".replace(os.path.sep, "__")
    _file = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "is_private": 0,
        "content": qr_image.getvalue()
    })
    _file.save()
	
