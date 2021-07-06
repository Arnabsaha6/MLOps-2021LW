function terminal() {
	var data = "cmdin";
	var url = "http://192.168.29.193/cgi-bin/app.py?x="
	cmdpmt(data,url);
}

function cmdpmt(data_id,url) {
  var xhr = new XMLHttpRequest();
  var i = document.getElementById(data_id).value 
  xhr.open("GET" , url  + i , true);
  xhr.send();
      
  xhr.onload = function() {
          var output = xhr.responseText;
          document.getElementById("cmdout").innerHTML = output ;
  }
}

var ifenter = document.getElementById("cmdin");

ifenter.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("submit_btn").click();
  }
});