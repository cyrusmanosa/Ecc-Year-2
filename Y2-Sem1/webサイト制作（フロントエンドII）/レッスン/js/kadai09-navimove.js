{
  const naviWrap = document.querySelector("#navi-wrap");
  const categoryNavi = document.querySelector("#category-navi ul");
  const categoryDl = document.querySelector(".category");
  const posY = naviWrap.offsetTop;

  window.onscroll = () => {
    let scroollTop = document.documentElement.scrollTop;
    categoryNavi.style.top = scroollTop >= posY ? `${scroollTop}px` : 0;
  };

  fetch("https://click.ecc.ac.jp/ecc/sakakura/ajax/selector-list.php")
    .then((response) => {
      return response.json();
    })
    .then((categories) => {
      console.log(categories);
      const Title = categories.selectors; 
      Title.forEach((e) => {
        let li = document.createElement("li");
        li.innerHTML = `<li>${e.category}</li>`;
        categoryNavi.appendChild(li);
      });
    })
}
