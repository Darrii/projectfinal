let inputs = document.getElementById("input_side")
let inputBtn = document.getElementById("inputBtn")
let searchBtn = document.getElementById("searchBtn")
let searches = document.getElementById("search_side")
function inputs_switcher(){
    display_style = inputs.style.display

    if(display_style == "none"){
        inputs.style.display = "flex"
        inputBtn.style.display = "none"
    }
    else{
        inputs.style.display = "none"
    }
}
function search_switcher(){
    display_style = searches.style.display

    if(display_style == "none"){
        searches.style.display = "flex"
        searchBtn.style.display = "none"
    }
    else{
        searches.style.display = "none"
    }

}
