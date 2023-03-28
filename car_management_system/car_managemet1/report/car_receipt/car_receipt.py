# Copyright (c) 2023, Ekanath and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = []
	data = []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns  = [{'fieldname':'user','label':'User','fieldtype':'Data'},
	{'fieldname':'car_type','lable':'Car Type','fieldtype':'Data'},
	{'fieldname':'car_books_for_days','lable':'Car Books For Days','fieldtype':'Int'},
	{'fieldname':'car_make','label':'Car Make','fieldtype':'Data'},
	{'fieldname':'car_model','label':'Car Model','fieldtype':'Data'},
	{'fieldname':'total_rent','label':'Total Rent','fieldtype':'Int'},
	{'fieldname':'transaction_id','label':'Transaction Id','fieldtype':'Data'}]
	return columns

def get_data(filters):
	conditions=""
	if ((filters.car_type)and (filters.car_make)):
		conditions += "and c.car_type = %(car_type)s"
		conditions +="and c.car_make = %(car_make)s"


	data = frappe.db.sql("""select c.user,c.car_type,c.car_books_for_days,c.car_make,c.car_model,c.total_rent,c.transaction_id from `tabCar Booking Receipt` as c where c.total_rent>=3000 {conditions}""".format(conditions=conditions),filters,as_dict=1)
	doc = frappe.get_all("Car Booking Receipt",["total_rent","car_books_for_days"])
	total = 0
	total1 = 0
	for i in doc:
		if i.total_rent>=3000:
			total1+=i.car_books_for_days
			total+=i.total_rent
	print("--------------------------",total)
	print("---------------------------",total1)
	data.append({
		"user":"",
		"car_type":"",
		"car_books_for_days":total1,
		"car_make":"",
		"car_model":"",
		"total_rent":total,
		"transaction_id":""
	})
	return data