{
  const Sub_btn = document.querySelector("[type=submit]");

  const U_v = document.getElementById("user_name");
  const A_v = document.getElementById("author_name");
  const PU_v = document.getElementById("product_url");
  const PC_v = document.getElementById("product_category");
  const VU_v = document.getElementById("video_url");
  const D_v = document.getElementById("description");

  const S = sessionStorage;
  
  const MN = new Map([
    ["user_name", U_v],
    ["author_name", A_v],
    ["product_url", PU_v],
    ["product_category", PC_v],
    ["video_url", VU_v],
    ["description", D_v],
  ]);

  Sub_btn.addEventListener("click", (e) => {
    e.preventDefault();
    MN.forEach((key, value) => {
      S.setItem(value, key.value);
    });
  });

  if (true) {
    MN.forEach((key, value) => {
      key.value = S.getItem(value);
    });
  }
}
