// Copyright (c) 2023, Ekanath and contributors
// For license information, please see license.txt

frappe.ui.form.on('User Management', {
	refresh: function(frm) {
		if(frm.doc.user_status !='Active'){

			frm.add_custom_button(('Car Return'),function(){
			frappe.call({
				method:"print_data",
				doc:frm.doc,
				callback:function(r){
					frappe.msgprint("car returned")
					console.log(r.message)
				}
			})
		 frm.set_value('car_booked', '')
		 frm.save()
		});
	}
},
});

