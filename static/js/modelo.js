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
});