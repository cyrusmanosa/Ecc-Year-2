
// document mouseover event
document.addEventListener('mousemove', (event)=>{
// client position
document.querySelector('#client').innerText = `${ event.clientX } : ${ event.clientY }`;
});
