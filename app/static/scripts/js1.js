var opc = ['Opción1', 'Opción2', 'Opción3'];
for(var i=0; i<opc.length; i++){
    var li_opc = document.createElement("li");
    li_opc.setAttribute('class', 'nav-item');
    
    var a_opc = document.createElement("a");
    a_opc.setAttribute('href', '#');
    a_opc.setAttribute('class', 'nav-link');
    var txt_opc = document.createTextNode(opc[i]);
    a_opc.appendChild(txt_opc);

    li_opc.appendChild(a_opc);
    //document.getElementById("nav_example").appendChild(li_opc);
}