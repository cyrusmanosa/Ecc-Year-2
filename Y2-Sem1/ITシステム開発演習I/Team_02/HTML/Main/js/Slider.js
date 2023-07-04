{
  const slide = document.querySelectorAll(".slide");
  let flag = 0;

  setInterval(() => {

    if (flag == slide.length) flag = 0;

    if (flag != slide.length + 1) {
      slide[flag].classList.remove("Sactive");
      
      if (flag + 1 === slide.length) {
        slide[0].classList.add("Sactive");
      }else{
        slide[flag + 1].classList.add("Sactive");
      }

      flag++;
    }
  }, 5000);
}
