{
  const doc = document;
  const text = doc.querySelector("input");
  const BtnSub = doc.querySelector("[type=submit]");
  const todo = doc.querySelector(".todo");
  const TB = todo.querySelector("tbody");
  const TR = doc.createElement("tr");


  BtnSub.addEventListener("click", (e) => {
    e.preventDefault();
    const row = TR.cloneNode(true);
    row.insertAdjacentHTML( "afterbegin",
    `   
      <td class="comment">${text.value}</td>
      <td class="control"><button type="button" class="remove">削除</button></td>
    `
    );
    TB.append(row);
  });

  
  todo.addEventListener("click", (e) => {
    const This = e.target;
    if (This.classList.contains("remove")) {
      const Thisrow = This.closest("tr");
      Thisrow.remove();
    }
  });
}
