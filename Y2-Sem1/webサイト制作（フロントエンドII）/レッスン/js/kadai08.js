let input = document.querySelector("input");
let deleteButton = document.querySelector(".remove");
const plusButton = document.querySelector("button");
const array = [];

plusButton.addEventListener("click", (e) => {
  e.preventDefault();
  let inputValue = input.value;
  if (true) {
    array.push(inputValue);
    localStorage.setItem("saveItem", JSON.stringify(array));
    render();
  }
});

  let deleteList = (e) => {
    let dleValue = JSON.parse(localStorage.getItem("saveItem"));
    let index = dleValue.indexOf(e);
    if (index > -1) {
      dleValue.splice(index, 1);
      localStorage.setItem("saveItem", JSON.stringify(dleValue));
      array.splice(index, 1);
      render();
    }
};

window.onload = () => {
  let localValue = localStorage.getItem("saveItem");
  if (localValue) {
    array.push(...JSON.parse(localValue));
    render();
  }
};

function render(){
  let resultHTML = "";
  for (let i = 0; i < array.length; i++) {
    resultHTML += `<tr>
    <td class="comment">${array[i]}</td>
    <td class="control"><button type="button" onclick="deleteList('${array[i]}')">削除</button></td>
    </tr>`;
  }
  document.querySelector("tbody").innerHTML = resultHTML;
};