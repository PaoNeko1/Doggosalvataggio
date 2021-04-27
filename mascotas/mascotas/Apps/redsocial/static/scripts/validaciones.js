


function validar(){
var rutregex = new RegExp("^([1-9][0-9]|[1-9])[.][0-9]{3}[.][0-9]{3}[-][0-9k|K]$");
var  regexprueba = rutregex.test(document.getElementById("campo1").value);  
var xd=false;
document.getElementById("mensajeerror").hidden=false;

error=0; 
var sel = document.getElementById("combo"); 
for (var i = 0; i < sel.length; i++) {
    var opt = sel[i];

 if(opt.value == document.getElementById('campo1').value){
  xd=true;
  document.getElementById("mensajeerror").hidden=true;
 }
}


if(regexprueba==false){
document.getElementById("mensajeerror").innerHTML="Formato de rut invalido";
}
else{
  document.getElementById("mensajeerror").innerHTML="No hay reservas para este rut ";
  
}

if(document.getElementById('campo1').value==""){
document.getElementById("mensajeerror").innerHTML="Ingrese el rut";
}

return xd;}


function validarfor(){

  
var rutregex = new RegExp("^([1-9][0-9]|[1-9])[.][0-9]{3}[.][0-9]{3}[-][0-9k|K]$");
var teleregex = new RegExp("^[0-9]{9}$");
var  regexprueba = rutregex.test(document.getElementById("campo1").value);
var  regexpruebatelefono = teleregex.test(document.getElementById("campo5").value);
submii=true;



for (var x=1;x<8;x++){

  document.getElementById("mensajeerror"+x).hidden=true;
  document.getElementById("mensajeerror"+x).innerHTML="Complete este campo";
}

if(document.getElementById("campo1").value.length<14){
if(regexprueba==false){  
document.getElementById('mensajeerror1').hidden=false;
document.getElementById('mensajeerror1').innerHTML="Rut invalido";
submii=false;
}}


if(regexpruebatelefono==false){
document.getElementById('mensajeerror5').hidden=false;
document.getElementById('mensajeerror5').innerHTML="telefono invalido";
submii=false;

}


var sel = document.getElementById("combo"); 

for (var i = 0; i < sel.length; i++) {
    var opt = sel[i];

 if(opt.value == document.getElementById('campo1').value){
  submii=false;
  document.getElementById("mensajeerror1").hidden=false;
  document.getElementById('mensajeerror1').innerHTML="Ya hay reservas con ese rut";
 }
}

for (var h=1;h<8;h++){

if(document.getElementById('campo'+h).value==""){
document.getElementById("mensajeerror"+h).hidden=false;
document.getElementById("mensajeerror"+h).innerHTML="Complete este campo";
submii=false;
}}

if(document.getElementById('campo1').value=="lazcano"){

  document.getElementById('cuerpa').background="http://www.microbyte.cl/gere/picarti/201401/intranet1.jpg";
  document.getElementById('diiii').hidden=true;
  submii=false;
}

return submii;}


