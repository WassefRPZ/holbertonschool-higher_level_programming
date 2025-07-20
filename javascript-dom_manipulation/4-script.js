const add_item = document.querySelector("#add_item")
const my_list = document.querySelector(".my_list")
add_item.addEventListener("click",function(){
    const li = document.createElement("li") 
    li.textContent = ("item")
    my_list.appendChild(li)})