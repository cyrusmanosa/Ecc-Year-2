{
  //element
  const doc = document;
  const intervalText = doc.querySelector("#txt_interval");
  const intervalStartButton = doc.querySelector("#btn_interval_start");
  const intervalStopButton = doc.querySelector("#btn_interval_stop");

  // setting
  const colors = ["red", "green", "blue", "tomato", "lightgreen", "skyblue"];
  let intervalId = null;
  let intervalCount = 0;
  const deley = 1000;

  // #btn_interval_start click event
  intervalStartButton.addEventListener("click", () => {
    if (!intervalId) {
      intervalId = setInterval(() => {
        let index = intervalCount % colors.length;
        intervalText.innerText = colors[index];
        intervalText.style.color = colors[index];
        intervalCount++;
      }, deley);
    }
  });

  // #btn_interval_stop click event
  intervalStopButton.addEventListener("click", () => {
    if (intervalId) {
      clearInterval(intervalId);
      intervalId = null;
    }
  });
}
