{
  let imgCount = 1;
  let img = document.querySelector("img");

  setInterval(() => {
    if (imgCount > 13) {
      imgCount = 1;
    }
    img.src = `../img/KD5/img-kadai05-00${imgCount}.jpg`;
    imgCount++;
  }, 3000);

  const year = document.querySelector("#year");
  let date = new Date();
  year.innerText = date.getFullYear();

}