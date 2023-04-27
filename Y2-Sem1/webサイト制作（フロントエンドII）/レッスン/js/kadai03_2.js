{
  const NW = document.querySelector("#navi-wrap");      // 引入目錄
  const CN = document.querySelector("#category-navi");  // 引入目錄 CSS
  const NWTop = NW.offsetTop;                           // 目錄頂點高度變數

  window.onscroll = (event) => {
    let rollY = document.documentElement.scrollTop;     // roll event
    if (rollY >= NWTop){                                // if roll數 多或等於頂點的高度
        CN.style.top = `${rollY}px`;                    // CSS的Top數 ＝ roll數 
    }else{
        CN.style.top = `0px`;                           // 回到初點
    }
  };
  // 目錄外層（navi-wrap）的relative. 所以目錄與頂點會隔開

  const year = document.querySelector("#year");
  let date = new Date();
  year.innerText = date.getFullYear();
}
