// document mouseover event
document.addEventListener('mousemove', (event)=>{
    // client position
    document.querySelector('#client').innerText = `${ event.clientX } : ${ event.clientY }`;
    // screen positioin
    document.querySelector('#screen').innerText = `${ event.screenX } : ${ event.screenY }`;
    // global positioin
    document.querySelector('#global').innerText = `${ document.documentElement.scrollLeft + event.clientX } : ${ document.documentElement.scrollTop + event.clientY }`;
  });