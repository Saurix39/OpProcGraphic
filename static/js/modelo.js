let left = 3;
let right = 1;

document.addEventListener('DOMContentLoaded', () => {

    const info_pages = document.querySelectorAll('.info-page');
    info_pages.forEach((elemento)=>{
        elemento.style.width = `calc( 100% / ${info_pages.length})`
    })
    const slider = document.querySelector('.slider');

    slider_pages = info_pages.length;
    left = slider_pages;
    slider.style.width = `${slider_pages}00%`;
    
    
    document.querySelector(".btn-left").onclick = () =>{
        selected =  document.querySelector(".slider");
        if(left < slider_pages && left > 0){
            selected.style.marginLeft = `${(selected.style.marginLeft == "0%" || selected.style.marginLeft == "" ? 0 : parseInt(selected.style.marginLeft)) + 100}%`;
            left++;
            right--;
        }       
    }

    document.querySelector(".btn-right").onclick = () =>{
        selected =  document.querySelector(".slider");
        if(right < slider_pages && right > 0){
            selected.style.marginLeft =  `${(selected.style.marginLeft == "" ? 0 : parseInt(selected.style.marginLeft)) - 100}%`;
            left--;
            right++;
        }
    }

    /** FASE 1*/
    /*Calculado tamaño de tablas*/
    const tables_fase1 = document.querySelectorAll(".table-fase1");
    tables_fase1.forEach((table, index) =>{
        tables_fase1[index].style.width = `calc( 100% / ${tables_fase1.length} - 4em)`
    })


    const carrousel__container = document.querySelector(".carrousel__container");
    carrousel__container.style.width = 100 * tables_fase1.length + '%';
    
    const puntos = document.querySelectorAll(".punto");
    puntos[0].classList.add('activo')
    puntos.forEach( (punto, position)=>{
        puntos[position].addEventListener("click", ()=>{
            calcWidth = position * (-100/tables_fase1.length) // 50 equivale al porcentaje que moveremos de translate X 
            carrousel__container.style.transform = `translateX(${ calcWidth }%)`;

            puntos.forEach( (punto, position) => {
                puntos[position].classList.remove('activo');
            })

            puntos[position].classList.add('activo');
        })
    })

    /** FASE 2*/
    /*Calculado tamaño de tablas*/
    // const tables_fase2 = document.querySelectorAll(".table-fase2");
    // tables_fase2.forEach((table, index) =>{
    //     tables_fase2[index].style.width = `calc( 100% / ${tables_fase2.length} - 4em)`
    // })


    // const carrousel__container_fase2 = document.querySelector(".carrousel__container-fase2");
    // carrousel__container_fase2.style.width = 100 * tables_fase2.length + '%';
    
    // const puntos_fase2 = document.querySelectorAll(".punto-fase2");
    // puntos_fase2[0].classList.add('activo')
    // puntos_fase2.forEach( (punto, position)=>{
    //     puntos_fase2[position].addEventListener("click", ()=>{
    //         calcWidth = position * (-100/tables_fase2.length) // 50 equivale al porcentaje que moveremos de translate X 
    //         carrousel__container_fase2.style.transform = `translateX(${ calcWidth }%)`;

    //         puntos_fase2.forEach( (punto, position) => {
    //             puntos[position].classList.remove('activo');
    //         })

    //         puntos_fase2[position].classList.add('activo');
    //     })
    // })
});