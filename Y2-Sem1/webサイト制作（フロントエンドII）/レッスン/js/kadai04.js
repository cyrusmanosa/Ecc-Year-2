{
let B = document.querySelectorAll('.blank')
let List = document.querySelectorAll('.list')

for (const property in B){
    B[property].target = List[property].alt
}

const year = document.querySelector("#year");
let date = new Date();
year.innerText = date.getFullYear();
}
