let left = 3;
let right = 1;

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector(".btn-left").onclick = () =>{
        selected =  document.querySelector(".slider");
        if(left < 3 && left > 0){
            selected.style.marginLeft = `${(selected.style.marginLeft == "" ? 0 : parseInt(selected.style.marginLeft)) + 100}%`;
            left++;
            right--;
        }       
    }

    document.querySelector(".btn-right").onclick = () =>{
        selected =  document.querySelector(".slider");
        if(right < 3 && right > 0){
            selected.style.marginLeft =  `${(selected.style.marginLeft == "" ? 0 : parseInt(selected.style.marginLeft)) - 100}%`;
            left--;
            right++;
        }
    }

    const grande = document.querySelector(".grande");
    const puntos = document.querySelectorAll(".punto");

    puntos.forEach( (punto, position)=>{
        puntos[position].addEventListener("click", ()=>{
    
            calcWidth = position * -50 // 50 equivale al porcentaje que moveremos de translate X 
            console.log(calcWidth)
            grande.style.transform = `translateX(${ calcWidth }%)`;
        })
    })
});