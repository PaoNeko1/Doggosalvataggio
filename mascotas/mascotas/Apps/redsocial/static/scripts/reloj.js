


num=0
(function(){

var saludo=function(){



var now = new Date().toTimeString();

document.getElementById('fecha').innerHTML=  now.substr(0,8);

};

setInterval(saludo,100);

}())
