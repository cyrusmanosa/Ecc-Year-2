{
  const u_text = document.querySelector("#user");
  const p_text = document.querySelector("#post");
  const ok_text = document.querySelector("#ok");
  const user_target = 2310;
  const post_target = 1320;
  const ok_target = 590;
  let a = 0;
  let b = 0;
  let c = 0;

  let inter = setInterval(() => {
    u_text.innerText = a;
    if (a == user_target) clearInterval(inter);
    a+=10;
    a++;
  }, 1);

  let inter2 = setInterval(() => {
    p_text.innerText = b;
    if (b == post_target) clearInterval(inter2);
    b+=5;
    b++;
  }, 1);

  let inter3 = setInterval(() => {
    ok_text.innerText = c;
    if (c == ok_target) clearInterval(inter3);
    c+=2;
  }, -5);
}