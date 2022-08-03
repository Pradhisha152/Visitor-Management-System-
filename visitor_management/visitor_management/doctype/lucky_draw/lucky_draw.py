# Copyright (c) 2022, thirvusoft and contributors
# For license information, please see license.txt
from os import environ
import random
import frappe
from frappe.model.document import Document

class LuckyDraw(Document):
	pass

@frappe.whitelist()
def random_pick(cnt,evn):
	lst = frappe.db.get_list("Registration F1",filters={"event":evn,"winner":0},pluck='name')
    
	print(lst)
	
	winners=[]
	for i in range(0,int(cnt),1):
		val = random.randint(0,len(lst)-1)
		if lst[val] in winners :
			while (lst[val]  in winners ):
				val = random.randint(0,len(lst)-1)
		var2 = frappe.get_doc("Registration F1",lst[val])
		print(var2)
		var2.winner =1
		var2.save()
		winners.append(lst[val])
       
		
	
	
	return winners 

   