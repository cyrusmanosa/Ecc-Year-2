const slide = document.querySelectorAll("li");
const show = document.querySelectorAll(".show")
const L = document.querySelector("#logo")
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
    if ( index == 0 ) {
      slide[0].style.zIndex = 1;
    }else{
      slide[0].style.zIndex = 0;
    }
    next.classList.add("show");
  }, 1000);
}, 3000);

