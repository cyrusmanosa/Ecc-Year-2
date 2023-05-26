{

  // element
  const doc = document;
  const list = doc.querySelector('#list');
  const listText = doc.querySelector('#list_text');
  const addButton  = doc.querySelector('#btn_add');
  const removeAllButton = doc.querySelector('#btn_remove_all');

  // setting
  const listElementTagName = 'li';
  const listItemTemplate = doc.createElement(listElementTagName);
  console.log(listItemTemplate);

  // #btn_add click event
  // リスト項目の追加
  addButton.addEventListener('click', (e)=>{
    let text = listText.value;

    if( text ) {
      // listItemTemplateをappendすると１回しか追加できない。
      const listItem = doc.createElement(listElementTagName);
      console.log(listItem);
      listItem.innerText = text;
      list.append(listItem);
    }
  });

  // #btn_remove_all click event
  // リスト項目のすべて削除
  removeAllButton.addEventListener('click', (e)=>{ 
    const listItems = list.querySelectorAll('li');
    listItems.forEach((listItem)=>{
      listItem.remove();
    });
  });

  // #list > li click event
  // クリックしたリスト項目へ目印をつける
  list.addEventListener('click', (e) => {
    console.log(e.target);
    const target = e.target;
    if(target.tagName == 'LI') {
      target.style.backgroundColor = 'tomato';
    }
  });

}