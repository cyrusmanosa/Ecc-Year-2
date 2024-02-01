const listBox = document.querySelector(".list-box");
const itemsPerPage = 12;
let page = 1;
let totalPages = 0;

async function fetchData() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    const data = await response.json();
    const startIndex = (page - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;

    totalPages = Math.ceil(data.length / itemsPerPage);
    console.log(totalPages);
    const currentPageData = data.slice(startIndex, endIndex);
    currentPageData.forEach((item) => {
      listBox.innerHTML += `
        <div class="item">
          <img src="./img/notebook.png" alt="" />
          <p class="name">${
            item.title == null || item.title == ""
              ? "タイトルがありません。"
              : item.title.length > 15
              ? item.title.substring(0, 15) + "..."
              : item.title
          }</p>
          <p class="location">${
            item.body == null || item.body == ""
              ? "内容がありません"
              : item.body.length > 20
              ? item.body.substring(0, 20) + "..."
              : item.body
          }</p>
          <p class="price">値段</p>
          <p class= "status">取引中</p>
        </div>
      `;
    });
    console.log(data);

    pagenation(); // 페이지네이션 업데이트
  } catch (error) {
    // 오류 처리
    console.error(error);
  }
}

const pagenation = () => {
  let pagenationHTML = "";
  let pageGroup = Math.ceil(page / 5);
  let last = pageGroup * 5;

  if (last >= totalPages) {
    last = totalPages;
  }
  let first = last - 4 <= 0 ? 1 : last - 4;

  pagenationHTML = `<li class="page-item">
  <a class="page-link" href="#" aria-label="Previous"onclick="moveToPage(${
    first > 1 ? 1 : 1
  })">
    <span aria-hidden="true">&lt;&lt;</span>
  </a>
</li>`;

  pagenationHTML += `<li class="page-item">
  <a class="page-link" href="#" aria-label="Previous"onclick="moveToPage(${
    page - 1 == 0 ? 1 : page - 1
  })">
    <span aria-hidden="true">&lt;</span>
  </a>
</li>`;

  for (let i = first; i <= last; i++) {
    pagenationHTML += `<li class="page-item ${
      page == i ? "active current" : ""
    }"><a class="page-link" href="#" onclick="moveToPage(${i})">${i}</a></li>`;
  }

  pagenationHTML += `<li class="page-item">
  <a class="page-link" href="#" aria-label="Next" onclick="moveToPage(${
    page + 1 >= totalPages ? totalPages : page + 1
  })">
    <span aria-hidden="true">&gt;</span>
  </a>
</li>`;

  pagenationHTML += `<li class="page-item">
<a class="page-link" href="#" aria-label="Next" onclick="moveToPage(${totalPages})">
  <span aria-hidden="true">&gt;&gt;</span>
</a>
</li>`;
  document.querySelector(".pagination").innerHTML = pagenationHTML;
};
function moveToPage(pageNum) {
  page = pageNum;
  console.log(page);
  window.scrollTo({ top: 0, behavior: "smooth" });
  listBox.innerHTML = ""; // 이전에 출력된 데이터를 초기화합니다.
  fetchData();
  pagenation(); // 페이지네이션 업데이트
}
pagenation();
fetchData();
