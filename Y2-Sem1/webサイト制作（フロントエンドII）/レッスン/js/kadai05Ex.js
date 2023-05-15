const slide = document.querySelectorAll("li");
const sliders = document.getElementById("slider");
let index = 0;


function nextImage() {  
  setTimeout(function(){slide[index].style.opacity = 0;},4000);
  index++;
  
  slide[index].style.opacity = 100;
  if (index + 1 > slide.length) {index = 1;} else {index++;}
}

function startSlideshow() {
  index=0;

  slide[index].style.opacity = 100;
  setTimeout(() =>{slide[index].style.opacity = 0;},4000);
  setInterval(() =>{nextImage()}, 5000);
}

startSlideshow();