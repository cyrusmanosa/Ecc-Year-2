let cx = document.querySelector('#client-x');
let cy = document.querySelector('#client-y');

let sx = document.querySelector('#screen-x');
let sy = document.querySelector('#screen-y');

let gx = document.querySelector('#global-x');
let gy = document.querySelector('#global-y');

document.addEventListener('mousemove', logKey);

function logKey(e) 
{
    cx.value=`${e.clientX}`;
    cy.value=`${e.clientY}`;

    sx.value=`${e.screenX}`;
    sy.value=`${e.screenY}`;

    gx.value=`${ document.documentElement.scrollLeft + e.clientX }`;
    gy.value=`${ document.documentElement.scrollTop + e.clientY}`;

}
