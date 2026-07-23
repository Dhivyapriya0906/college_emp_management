// Department Chart

new Chart(document.getElementById("departmentChart"),{

type:"bar",

data:{

labels:["IT","HR","Admin","Accounts"],

datasets:[{

label:"Employees",

data:[15,8,5,7],

backgroundColor:[
"#1E3A8A",
"#2563EB",
"#3B82F6",
"#60A5FA"
]

}]

},

options:{

responsive:true,

plugins:{
legend:{
display:false
}
}

}

});


// Leave Chart

new Chart(document.getElementById("leaveChart"),{

type:"doughnut",

data:{

labels:["Approved","Pending","Rejected"],

datasets:[{

data:[10,3,2],

backgroundColor:[
"#16A34A",
"#F59E0B",
"#DC2626"
]

}]

},

options:{

responsive:true

}

});