let left = 4;
let right = 1;

document.addEventListener('DOMContentLoaded', () => {

    // This event enable or disable the button
    document.querySelector("#ecuaciones").onkeyup = function (){
        if(this.value != null & this.value != ""){
            document.querySelector("#btnSent").disabled = false
        }else{
            document.querySelector("#btnSent").disabled = true;
        }
    }
    document.querySelector(".btn-left").onclick = () =>{
        selected =  document.querySelector(".slider");
        if(left < 4 && left > 0){
            selected.style.marginLeft = `${(selected.style.marginLeft == "" ? 0 : parseInt(selected.style.marginLeft)) + 100}%`;
            left++;
            right--;
        }       
    }

    document.querySelector(".btn-right").onclick = () =>{
        selected =  document.querySelector(".slider");
        if(right < 4 && right > 0){
            selected.style.marginLeft =  `${(selected.style.marginLeft == "" ? 0 : parseInt(selected.style.marginLeft)) - 100}%`;
            left--;
            right++;
        }
    }
});