const listItems = document.querySelectorAll(".sidebar-list li");
const id=document.querySelector(".id-filme")
let botaoComprar=document.querySelector('#ComprarIngresso')
const sala=document.querySelector('#id_sala')
const projecao=document.querySelector('#id_projecao')

listItems.forEach((item) => {
    item.addEventListener("click", () => {
        let isActive = item.classList.contains("active");

        listItems.forEach((el) => {
            el.classList.remove("active");
        });

        if (isActive) item.classList.remove("active");
        else item.classList.add("active");
    });
});

/* busca.event('click',function(event){
    event.preventDefault();
    filme=id;
}); */
/* sala.addEventListener("change", () => {
    console.log(sala.options[sala.selectedIndex].text);
    console.log(sala.selectedIndex.projecao)
    projecao.value=sala.selectedIndex.projecao
}); */
