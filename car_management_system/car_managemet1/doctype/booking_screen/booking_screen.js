// Copyright (c) 2023, Ekanath and contributors
// For license information, please see license.txt

frappe.ui.form.on('Booking Screen', {
	refresh: function(frm) {
	   frm.add_custom_button(('Fetch Car Details'),function(){
		frm.clear_table("car_details")
		frappe.call({
			method:"print_data",
			doc:frm.doc,
			callback:function(r){
				frm.refresh_field("car_details")
				console.log(r.message)
			}
		})
	   });
	},
	
});

frappe.ui.form.on('Booking Screen', {
	refresh: function(frm) {
	   frm.add_custom_button(('Car Booked'),function(){
		frappe.call({
			method:"car_booked",
			doc:frm.doc,
			callback:function(r){
				frappe.msgprint("car booked")
				frm.refresh_field("total_rent")
				console.log(r.message)
			}
		})
	   });
	},
	
});


frappe.ui.form.on('Car Details',{
	car_book: function(frm, cdt, cdn) {
        var child_table = locals[cdt][cdn];
		console.log("123456",child_table)
        if (child_table.car_book) {
			console.log("6789")
            $.each(frm.doc.car_details || [], function(i, row) {
                if (row.name != child_table.name && row.car_book) {
                    frappe.model.set_value(row.doctype, row.name, 'car_book', false);
                }
            });
        }
		console.log("1234567890")
    }

});