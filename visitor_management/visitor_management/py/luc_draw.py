import frappe
import erpnext
from frappe import _
import random
import json

def random_pick(cnt):
   lst = frappe.db.get_value("Event","EV00001","registration_detials")
   winners=[]
   for i in range(cnt):
       val = random.randint(0,len(lst))
       winners.append(lst[val])
   return winners 
