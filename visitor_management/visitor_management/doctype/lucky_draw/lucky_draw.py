# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt
import random
import frappe
from frappe.model.document import Document

class LuckyDraw(Document):
	pass

@frappe.whitelist()
def random_pick(cnt,evn):
	registered_list = frappe.db.get_list("Registration Form",filters={"event":evn,"winner":0},pluck='name')
	winners=[]
	for i in range(0,int(cnt),1):
		lucky_num = random.randint(0,len(registered_list)-1)
		frappe.db.set_value("Registration Form",registered_list[lucky_num],"winner",1)
		winners.append(registered_list[lucky_num])
		registered_list.remove(registered_list[lucky_num])
	return winners 

   