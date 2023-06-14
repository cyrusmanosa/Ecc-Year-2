{
  const doc = document;
  const text = doc.querySelector("input");
  const BtnSub = doc.querySelector("[type=submit]");
  const todo = doc.querySelector(".todo");
  const TB = todo.querySelector("tbody");
  const TR = doc.createElement("tr");
  
  // let Data;
  // let Jdata = [];
  // let jsonString = JSON.stringify(Jdata);
  
  BtnSub.addEventListener("click", (e) => {
    e.preventDefault();
    if (text.value != "" && text.value != null) {
      const row = TR.cloneNode(true);
      row.insertAdjacentHTML(
        "afterbegin",
        `   
        <td class="comment">${text.value}</td>
        <td class="control"><button type="button" class="remove">削除</button></td>
        `
        );
        TB.append(row);
        
      // Jdata += {Commet : text.value};
      
      // jsonString += JSON.stringify(Jdata)
      // Data = jsonString
      // localStorage.setItem("Web_Kadai08", jsonString);
    }
  });

  // Remote
  todo.addEventListener("click", (e) => {
    const This = e.target;
    if (This.classList.contains("remove")) {
      const Thisrow = This.closest("tr");
      Thisrow.remove();
    }
  });

  // Year num
  {
    const year = document.querySelector("#year");
    let date = new Date();
    year.innerText = date.getFullYear();
  }
}
