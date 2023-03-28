// Copyright (c) 2023, Ekanath and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Car Receipt"] = {
	"filters": [
		{
			"fieldname":"car_type",
			"label":"Car Type",
			"fieldtype":"Select",
			"options":['SUV','Sedan','Hetchback']
			
		},
		{
			"fieldname":"car_make",
			"label":" Car Make",
			"fieldtype":"Data",
		}
	]
};
