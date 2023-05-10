{
  const todoList = document.querySelector("#todo_list");
  // console.log(todoList);
  // const todoListItem = docment.querySelectorAll('.item');
  const todoListItems = todoList.querySelectorAll(".item");
  const todoListItems2 = todoList.querySelectorAll(".item");
  console.log(todoListItems);
  console.log(todoListItems2);

  todoListItems.forEach((value,key) =>{
    console.log(`${key} : ${value}`);
    value.style.backgroundColor = "red";
  });


  const object = { a:1 , b:2 , c:3 };
  for (const property in object){
    console.log(property + ":" + object[property])
  }

  const link = document.querySelector('#link');
  link.addEventListener('click',(e) =>{
    e.preventDefault();
    window.open(e.target.href,'.blank');
    console.log('クリックしたよ');
  });
}
