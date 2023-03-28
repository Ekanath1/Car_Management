# Copyright (c) 2023, Ekanath and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ReportAnalysis(Document):
	def before_save(self):
		doc = frappe.db.get_all('Car')
		length = len(doc)
		if length>0:
			self.total_cars = length
		doc1 = frappe.db.get_all('Car',filters={"car_status":"Available"})
		length1 = len(doc1)
		print(".......................available......................",length1)
		if length1>0:
			self.car_available = length1
		doc2 = frappe.db.get_all('Car',filters={"car_status":"Issued"})
		length2 = len(doc2)
		print("...................issued..........................",length2)
		if length2>0:
			self.car_rented = length2
		doc3 = frappe.db.get_all('User Management',filters={"user_status":"Active"})
		length3 = len(doc3)
		print("....................Active......",length3)
		if length3>0:
			self.active_user = length3
		doc4 = frappe.db.get_all('User Management',filters={"user_status":"Using Car"})
		length4 = len(doc4)
		print("......................Using Car..............................",length4)
		if length4>0:
			self.user_using_car = length4