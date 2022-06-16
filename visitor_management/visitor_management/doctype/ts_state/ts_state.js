// Copyright (c) 2022, thirvusoft and contributors
// For license information, please see license.txt
frappe.ui.form.on('TS State', {
	state : function(frm) {
	if(frm.doc.state === "Tamil Nadu"){
		frm.set_df_property("district", "options", "");
	   frm.set_df_property("district", "options", [
		'Ariyalur',
		'Chennai',
		'Coimbatore',
		'Cuddalore',
		'Dharmapuri',
		'Dindigul',
		'Erode',
		'Kanchipuram',
		'Kanyakumari',
		'Karur',
		'Madurai',
		'Nagapattinam',
		'Nilgiris',
		'Namakkal',
		'Perambalur',
		'Pudukkottai',
		'Ramanathapuram',
		'Salem',
		'Sivaganga',
		'Tirupur',
		'Tiruchirappalli',
		'Theni',
		'Tirunelveli',
		'Thanjavur',
		'Thoothukudi',
		'Tiruvallur',
		'Tiruvarur',
		'Tiruvannamalai',
		'Vellore',
		'Viluppuram',
		'Virudhunagar',
]);
	}
	else if(frm.doc.state === "Maharashtra"){
		frm.set_df_property("district", "options", "");
	   frm.set_df_property("district", "options", [
		'Ahmednagar',
		'Akola',
		'Amravati',
		'Aurangabad',
		'Bhandara',
		'Beed',
		'Buldhana',
		'Chandrapur',
		'Dhule',
		'Gadchiroli',
		'Gondia',
		'Hingoli',
		'Jalgaon',
		'Jalna',
		'Kolhapur',
		'Latur',
		'Mumbai City',
		'Mumbai suburban',
		'Nandurbar',
		'Nanded',
		'Nagpur',
		'Nashik',
		'Osmanabad',
		'Parbhani',
		'Pune',
		'Raigad',
		'Ratnagiri',
		'Sindhudurg',
		'Sangli',
		'Solapur',
		'Satara',
		'Thane',
		'Wardha',
		'Washim',
		'Yavatmal',
	]);
	frm.refresh_field("district");}
	},
	district:function(frm){
		frm.set_value("name1",frm.doc.district);
	}
});