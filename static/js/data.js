
document.addEventListener('DOMContentLoaded', () =>{

    let form = document.querySelector("#form-data");

    form.addEventListener('submit', onsubmit);


})

function sent(data){
    const request = new XMLHttpRequest();

    request.open('POST', 'http://127.0.0.1:5000/getData')

    request.onload = () => {
        console.log("Works");
    }

    const d = new FormData();
    d.append("MinMax", data["Minmax"]);
    d.append("Fo", JSON.stringify(data["Funcion objetivo"]));
    d.append("Restr", JSON.stringify(data["Restricciones"]));

    request.send(d)
}

function onsubmit(event){
    
    event.preventDefault();

    data = {
        "Minmax": document.querySelector("#minmax").value,
        "Funcion objetivo": getFuncionObjetivo(),
        "Restricciones": getRestricciones()
    }
    console.log(data)
    sent(data)

    return false;
}

function getFuncionObjetivo(){

    // Get the elements
    const inputs = document.querySelectorAll(".objFuncion");

    const f = {
        "x1": "",
        "x2": "",
    }

    if(inputs[0].value == null){
        inputs[0].classList.add('danger');
    }else if(inputs[1].value == null){
        inputs[1].classList.add('danger');
    }else{
        f['x1'] = inputs[0].value;
        f['x2'] = inputs[1].value
    }

    return f;
}


function getRestricciones(){

    const restricciones = [];

    const resFields = document.querySelectorAll(".Restricciones");

    resFields.forEach( elem => {
        restricciones.push({
            "x1": elem.querySelector(".resx1").value,
            "x2": elem.querySelector(".resx2").value,
            "op": elem.querySelector(".resOperand").value,
            "result": elem.querySelector(".resResult").value
        });
    });

    return restricciones;

}