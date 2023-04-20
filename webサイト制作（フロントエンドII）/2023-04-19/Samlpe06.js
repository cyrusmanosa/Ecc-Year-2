{
    // #sec01 click event
    document.querySelector('#sec01').addEventListener('click', (event)=>{
        document.querySelector('#sec01 > .pos').innerText = `${ event.currentTarget.offsetLeft } : ${ event.currentTarget.offsetTop }`;
    });
    // #sec02 click event
    document.querySelector('#sec02').addEventListener('click', (event)=>{
        document.querySelector('#sec02 > .pos').innerText = `${ event.currentTarget.offsetLeft } : ${ event.currentTarget.offsetTop }`;
    });
    
}