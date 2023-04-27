/**
 * コンテンツのリサイズ
 */
window.onload = (e) =>
{
    const cw = document.querySelector('#content-wrap');
    const header = document.querySelector('#wrapper > header');
    const footer = document.querySelector('#wrapper > footer');
    let winH = e.currentTarget.innerHeight;
    let headerH = header.clientHeight + 2;
    let footerH = footer.clientHeight;
    let cwH = cw.clientHeight;
    let siteH = headerH + cwH + footerH;

    if( winH > siteH ){
        cw.style.height = ( cwH + ( winH - siteH ) ) + 'px';
    }

    /**
     * コピーライトの年度更新
     */
    const year = document.querySelector('#year');
    let date = new Date();
    year.innerText = date.getFullYear();
    
    // BG Color
    const box1 = document.querySelector('#box1');
    const Ccode1 = document.querySelector('#set-bg-txt');
    document.querySelector('#box1-bg-btn').addEventListener('click',() => {
        box1.style.background = Ccode1.value;
    });

    // Word Color
    const box2 = document.querySelector('#box2-text');
    const Ccode2 = document.querySelector('#set-color-txt');
    document.querySelector('#box2-color-btn').addEventListener('click',() => {
        box2.style.color = Ccode2.value;
    });

    // Word size
    const box3 = document.querySelector('#box3-text');
    const Scode3 = document.querySelector('#set-font-size-txt');
    document.querySelector('#box3-font-size-btn').addEventListener('click',() => {
        box3.style.fontSize = Scode3.value;
    });

    // link
    const box4 = document.querySelector('#box4');
    const Lcode4 = document.querySelector('#set-border-txt');
    document.querySelector('#box4').addEventListener('click',() => {
        box4.style.border = Lcode4.value;
    });
}
