{
  const Myslider = document.querySelectorAll("#slider");
  let nIntervId;

  for (const F in Myslider) {
    if (!nIntervId) {
      nIntervId = setInterval(() =>{
        if (Myslider[F].style.display === "block"){
          Myslider[F].style.display = `none`;
        }else{
          Myslider[F].style.display = `block`;
        }
      }, 3000);
    }else{
        clearInterval(nIntervId);
        nIntervId = null;
    }
  }


  const year = document.querySelector("#year");
  let date = new Date();
  year.innerText = date.getFullYear();
}
