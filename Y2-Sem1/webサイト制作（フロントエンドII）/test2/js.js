{
  //element
  const intervalText = document.querySelector("#txt");

  // setting
  const deley = 100;
  const s = 2903;
  let intervalCount = 0;

  // #btn_interval_start click event
      let inter  = setInterval(() => {
        intervalText.innerText = intervalCount;
        if (intervalCount == s){
          clearInterval(inter);
        }
        intervalCount++;
      }, deley);
}
