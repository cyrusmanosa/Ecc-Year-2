{
  //element
  const doc = document;
  const timeoutText = doc.querySelector("#txt_timeout");
  const timeoutStartButton = doc.querySelector("#btn_timeout_start");
  const timeoutStopButton = doc.querySelector("#btn_timeout_stop");

  // setting
  let timerId = null;
  const deley = 2000;

  // #btn_timeout_start click event
  timeoutStartButton.addEventListener("click", () => {
    timeoutText.innerText = "タイマースタート";

    if (!timerId) {
      timerId = setTimeout(() => {
        timerId = null;
        timeoutText.innerText = "timeoutで設定した時間を経過";
      }, deley);
    }
    
  });

  // #btn_timeout_stop click event
  timeoutStopButton.addEventListener("click", () => {
    timeoutText.innerText = "タイマーストップ";
    if (timerId) {
      clearTimeout(timerId);
      timerId = null;
    }
  });
}
