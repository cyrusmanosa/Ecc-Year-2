const d = document
const B_img = d.querySelector('.BPP img')

const SI = new Map([
    ["S1" , d.querySelector('#g-c1-r1 img')], 
    ["S2" , d.querySelector('#g-c1-r2 img')], 
    ["S3" , d.querySelector('#g-c1-r3 img')], 
    ["S4" , d.querySelector('#g-c1-r4 img')], 
    ["S5" , d.querySelector('#g-c1-r5 img')], 
])


SI.forEach((key) =>{
    console.log(key.src)
    key.addEventListener('click', () =>{
        B_img.src = key.src
    })
})