const dealingListButton = document.querySelector(".deal-ing-btn");
const likeListButton = document.querySelector(".like-list-btn");
let imgSection = document.querySelector(".img-section");
const dealItem = document.querySelectorAll(".deal-ing-item");
const likeItems = document.querySelectorAll(".like-item");

const render = (items) => {
  console.log(items);
  imgSection.innerHTML = "";
  console.log(imgSection);
  items.forEach((e) => {
    imgSection.appendChild(e);
  });
};

render(dealItem);

dealingListButton.addEventListener("click", () => {
  dealingListButton.classList.remove("not-selected");
  likeListButton.classList.remove("selected");
  dealingListButton.classList.add("selected");
  render(dealItem);
});

likeListButton.addEventListener("click", () => {
  dealingListButton.classList.remove("selected"); //
  likeListButton.classList.remove("not-selected");
  likeListButton.classList.add("selected");

  render(likeItems);
});
//정보수정버튼을 클릭합니다
//정보수정버튼을 클릭하면 몇개의 정보들이 인풋으로 바뀝니다
//inout으로 바뀐거에 값을 입력하여 저장하기 버튼을 누룹니다
//저장하기버튼을 누르먄 입력했던 값으로 바껴져있습니다.
//마무리 코드 짧게 만들기--
const editInformationBtn = document.querySelector(".edit-information");
const informations = document.querySelectorAll(".information p");

editInformationBtn.addEventListener("click", () => {
  if (editInformationBtn.textContent === "個人情報編集") {
    informations.forEach((e) => {
      const input = document.createElement("input");
      const textarea = document.createElement("textarea");
      input.type = "text";
      textarea.type = "textarea";
      input.value = e.textContent;
      textarea.value = e.textContent;
      e.textContent = "";
      if (e.classList.contains("explan")) {
        console.log("Explain");
        e.appendChild(textarea);
      } else {
        e.appendChild(input);
      }
    });

    editInformationBtn.textContent = "SAVE";
  } else {
    informations.forEach((e) => {
      const input = e.querySelector("input");
      const textarea = e.querySelector("textarea");
      if (input) {
        const updatedInfo = input.value;
        e.textContent = updatedInfo;
      } else if (textarea) {
        const updatedInfo = textarea.value;
        e.textContent = updatedInfo;
      }
    });

    editInformationBtn.textContent = "個人情報編集";
  }
});
