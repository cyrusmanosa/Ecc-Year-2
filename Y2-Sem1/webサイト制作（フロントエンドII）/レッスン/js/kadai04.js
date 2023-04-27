let B = document.querySelectorAll('.blank')
let LName = document.querySelectorAll('img')

for( let i = 0; i < B.length; i++ ){
    B[i].target = LName[i].alt       
}