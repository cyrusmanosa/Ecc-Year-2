const slide = document.querySelectorAll("li");
const show = document.querySelectorAll(".show")
let index = 0;

setInterval(() => {
  let previous = slide[index == 0 ? slide.length - 1 : index - 1];
  let next = slide[index == slide.length - 1 ? 0 : index + 1];

  next.setAttribute("id", "next");
  previous.style.display = "none";


  slide[index].removeAttribute("id");
  slide[index].removeAttribute("class");

  index++;
  if (index == slide.length) {
    index = 0;
  }
  next.style.display = "block";

  setTimeout(() => {
    if ( next != slide[0]){
      next.classList.add("show");
    }
  }, 1000);
}, 3000);

