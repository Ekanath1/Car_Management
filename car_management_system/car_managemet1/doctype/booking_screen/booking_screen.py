# Copyright (c) 2023, Ekanath and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import string
import random

class BookingScreen(Document):
	#total = 0
	@frappe.whitelist()
	def car_booked(self):
		total = 0
		for j in self.car_details:
			if j.car_book == 1:
				total=j.car_rate*self.car_book_for_days
				# print("=============",total)
			self.total_rent = total
		cbr = frappe.new_doc('Car Booking Receipt')
		cbr.user = self.user,
		if self.total_rent>0:
			cbr.total_rent = self.total_rent
		if self.car_book_for_days>0:
			cbr.car_books_for_days = self.car_book_for_days
		for i in self.car_details:
			if i.car_book == 1:
				cbr.car_type = i.car_type,
				cbr.car_make = i.make,
				cbr.car_model = i.model,
		N = 7
		res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
		print("The generated random string : " + str(res))
		cbr.transaction_id = str(res),
		cbr.insert()
		for k in self.car_details:
			if k.car_book == 1:
				doc = frappe.get_doc("Car",{"car_make":k.make,"car_type":k.car_type,"car_model":k.model})
				doc.car_status="Issued"
				doc.save()
		
		doc = frappe.get_doc("User Management",{"name1":self.user})
		for m in self.car_details:
			if m.car_book == 1:
				doc.car_booked = m.make
				doc.save()

		frappe.db.sql("""
			UPDATE `tabUser Management`
			SET user_status = 'Using Car'
			WHERE
				name = '{0}'
		""".format(self.user))

	@frappe.whitelist()
	def print_data(self):
		doc1=frappe.db.get_all("Car",{"car_status":"Available"},['car_make','car_model','car_transmission','registration_number','car_rate_per_day','car_type'])
		for i in doc1:
			self.append("car_details",{
				"make":i.car_make,
				"model":i.car_model,
				"car_transmission":i.car_transmission,
				"registration_number":i.registration_number,
				"car_rate":i.car_rate_per_day,
				"car_type":i.car_type
			})
		return "hi this message from Ekanath"
	