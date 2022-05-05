// NAVIGATION BAR
function navbar() {
    var x = document.getElementById("nav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

// FORM Date

document.getElementById('date').valueAsDate = new Date();
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1;
var yyyy = today.getFullYear();
if(dd<10){
  dd='0'+dd;
} 
if(mm<10){
  mm='0'+mm;
} 

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("date").setAttribute("max", today);
var min_date = (yyyy-2)+'-'+mm+'-'+dd;
document.getElementById("date").setAttribute("min", min_date);

//FORM Submit

let table = document.getElementById("news_table").getElementsByTagName('tbody')[0];
let tabledata = JSON.parse(window.localStorage.getItem("local_data"));
let buttons = 0;
// console.log(tabledata);

for (var i = 0; tabledata && i < tabledata.length; i++) {
    var row = table.insertRow(i);
    row.id = "rows";
    var j = 0;
    var data = tabledata[i];

    for (entry in data) {
        var cell = row.insertCell(j++);
        cell.innerHTML = data[entry];
    }

}

function add() {
		for (const el of document.getElementById('form').querySelectorAll("[required]")) {
			if (!el.reportValidity()) {
				return;
			}
		}
    var date = document.getElementById("date").value;
    var importance = document.getElementById("imp").value;
    var title = document.getElementById("title").value;
    var data = document.getElementById("data").value;

    var to_push = {
        Date: date, Importance: importance,
        Level: title, News: data
    }
    var arr = [date, importance, title, data];

    var num_rows = table.rows.length;
    var row = table.insertRow(num_rows);
    row.id = "rows";

    for (let j = 0; j < arr.length; j++) {
        var cell = row.insertCell(j);
        cell.innerHTML = arr[j];
    }

    let stringdata = window.localStorage.getItem("local_data");
    if (stringdata) {
        var get_data = JSON.parse(stringdata);
        get_data.push(to_push);
        window.localStorage.setItem("local_data", JSON.stringify(get_data));
    }
    else {
        var create_list = [];
        create_list.push(to_push);
        window.localStorage.setItem("local_data", JSON.stringify(create_list));
    }
}

function cleardata() {
    window.localStorage.removeItem("local_data");
    table.innerHTML = "";
    location.reload();
    buttons = 0;
}

var font_size = 1.5;
function fontsize() {
    var elem = document.getElementById("news_table");

    if (font_size === 1) {
        elem.style.fontSize = "1.5rem";
        font_size = 1.5;
    }
    else if (font_size === 1.5) {
        elem.style.fontSize = "2.0rem";
        font_size = 2.0;
    }
    else if (font_size === 2) {
        elem.style.fontSize = "1.49rem";
        font_size = 1.49;
    }
    else if (font_size === 1.49) {
        elem.style.fontSize = "1.0rem";
        font_size = 1;
    }
}

var background_index = 0;
var background_color = ["black", "dimgray", "darkslategray", "rebeccapurple", "midnightblue"];
function background() {
    background_index = (background_index + 1) % 5;
    document.body.style.backgroundColor = background_color[background_index];
}
