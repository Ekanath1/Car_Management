# Copyright (c) 2023, Ekanath and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class UserManagement(Document):
	def validate(self):
		if self.age<18:
			frappe.throw("You must be 18 years or older ")
	@frappe.whitelist()
	def print_data(self):
		doc = frappe.get_doc("Car",{"car_make":self.car_booked})
		print("1111111111111111111111111111111111111111",doc)
		frappe.db.sql("""UPDATE `tabCar` SET car_status='Available' WHERE car_status='Issued' and car_make='{0}'""".format(self.car_booked))
		frappe.db.sql("""update `tabUser Management` set user_status='Active' where user_status='Using Car' and car_booked='{0}'""".format(doc.car_make))
		return "Hello"