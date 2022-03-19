let Nombre= document.getElementById("Name").value;
let Apellido= document.getElementById("LastName").value;
let Cedula= document.getElementById("C.I").value;



if (Nombre || Apellido == null && Cedula==0){
    alert("Debe de ingresar un valor")
}

