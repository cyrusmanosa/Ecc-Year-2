const naviWrap = document.querySelector("#navi-wrap");
const categoryNavi = document.querySelector("#category-navi");
const categoryNaviUl = document.querySelector("#category-navi ul");
const categoryNavili = categoryNaviUl.querySelector("li");
const categoryWrap = document.querySelector("#category-wrap");
const posY = naviWrap.offsetTop;

window.onscroll = () => {
  let scroollTop = document.documentElement.scrollTop;
  categoryNavi.style.top = scroollTop >= posY ? `${scroollTop}px` : 0;
};

fetch("https://click.ecc.ac.jp/ecc/sakakura/ajax/selector-list.php")
  .then((response) => { return response.json(); })
  .then((categories) => {
    const title = categories.selectors;
    // add data
    title.forEach((e) => {
      // category
      const li = document.createElement("li");
      li.textContent = e.category;
      categoryNaviUl.appendChild(li);
      // first time
      e.list.forEach((f) => {
        let B;
        B = `
          <div class="category">
            <h2>${f.category}</h2>
            <dl>
              <dt>${f.type}</dt>
              <dd>${f.range}</dd>
            </dl>
          </div>
        `;
        categoryWrap.innerHTML += B;
      });
      // all　items　btn 
      categoryNavili.addEventListener("click", () => {
        li.classList.remove("active");
        categoryNavili.classList.add("active");
        e.list.forEach((f) => {
          let B;
          B = `
            <div class="category">
              <h2>${f.category}</h2>
              <dl>
                <dt>${f.type}</dt>
                <dd>${f.range}</dd>
              </dl>
            </div>
          `;
          categoryWrap.innerHTML += B;
        });
      });
      // click item
      li.addEventListener("click", () => {
        categoryWrap.innerHTML = "";
        e.list.forEach((f) => {
          const category = `
          <div class="category">
            <h2>${f.category}</h2>
            <dl>
              <dt>${f.type}</dt>
              <dd>${f.range}</dd>
            </dl>
          </div>`;
          categoryWrap.insertAdjacentHTML("beforeend", category);
        });
      });
    });

    // category color change 
    const c = categoryNaviUl.querySelectorAll('li');
    c.forEach(li => {
      li.addEventListener('click', (e) => {
        for (let i = 0; i < c.length ; i++) {
          if (c[i].classList == 'active'){
            c[i].classList.remove('active');
          }
        }
        e.target.classList.add('active');
      });
    });
  });

const year = document.querySelector("#year");
let date = new Date();
year.innerText = date.getFullYear();
