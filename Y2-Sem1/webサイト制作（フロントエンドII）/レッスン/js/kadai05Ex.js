const slide = document.querySelectorAll("li");
let index = 0;

setInterval(() => {
  slide[index].style.display = "none";
  index++;
  if (index == slide.length) {index = 0;}
  slide[index].style.display = "block";
  slide.className += "show"
}, 3000);