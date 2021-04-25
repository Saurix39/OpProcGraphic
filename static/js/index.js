document.addEventListener('DOMContentLoaded', () => {

    // This event enable or disable the button
    document.querySelector("#ecuaciones").onkeyup = function (){
        if(this.value != null & this.value != ""){
            document.querySelector("#btnSent").disabled = false
        }else{
            document.querySelector("#btnSent").disabled = true;
        }
    }
});