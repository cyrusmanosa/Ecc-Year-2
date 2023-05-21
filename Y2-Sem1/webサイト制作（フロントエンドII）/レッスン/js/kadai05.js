{
  let imgCount = 2;
  let img = document.querySelector("img");
  let T = 0;

  setInterval(() => {
    if ( T == 1 && imgCount == 4){ T = 0; imgCount = 1;}
    img.src = `../img/KD5/img-kadai05-0${T}${imgCount}.jpg`;
    imgCount++;
    if (imgCount > 9) { T = 1; imgCount = 0}
  }, 3000);

  const year = document.querySelector("#year");
  let date = new Date();
  year.innerText = date.getFullYear();
}



// const slide = document.querySelectorAll("li");
// let index = 0;

// setInterval(() => {
//   slide[index].style.display = "none";
//   index++;
//   if (index == slide.length) {index = 0;}
//   slide[index].style.display = "block";
// }, 3000);

