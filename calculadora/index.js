//Clear
//aca se crea evento para limpiar el display de la calculadora
document.querySelector("#clear").addEventListener("click", ()=>{
    document.querySelector("#display").value = " ";
})

//backSpace
//aca se crea funcion para restar unidad por unidad en el numero ingresado, se llama con un onclick
const backspace = ()=> {
    const num = document.querySelector("#display").value.slice(0, -1);
    document.querySelector("#display").value = num;
}

//1
const uno = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "1";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "1";
    }
}
//2
const dos = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "2";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "2";
    }
}
//3
const tres = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "3";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "3";
    }
}
//4
const cuatro = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "4";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "4";
    }
}
//5
const cinco = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "5";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "5";
    }
}
//6
const seis = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "6";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "6";
    }
}
//7
const siete = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "7";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "7";
    }
}
//8
const ocho = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "8";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "8";
    }
}
//9
const nueve = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "9";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "9";
    }
}
//0
const cero = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = "0";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + "0";
    }
}

//point
const point = ()=> {
    if(document.querySelector("#display").value == " "){
        document.querySelector("#display").value = ".";
    }
    else{
        document.querySelector("#display").value = document.querySelector("#display").value + ".";
    }
}