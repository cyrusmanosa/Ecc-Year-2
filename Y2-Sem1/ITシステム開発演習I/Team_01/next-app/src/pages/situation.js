import { useState } from "react";
import style from "../styles/situation.module.css";
import movePage from "./_route";
const situation = () => {
  const titles = ["あなたの安否状況を教えて下さい。", "怪我をしていますか？", "けがの度合いは？", "周囲は安全ですか？", "避難はできますか？"]
  const texts = [["無事です", "被害あり"], ["怪我無し", "怪我有り"], ["軽傷", "重傷"], ["安全", "危険"], ["はい", "いいえ"]]
  const [state, setState] = useState(0);
  const [data, setData] = useState([undefined, undefined, undefined, undefined, undefined]);
  const default_change = () => setState(state + 1);
  const end = () => {
    console.log("end");
    console.log(data);
    movePage("Homepage")()
  }

  const states = [
    (input) => {
      if (input !== 0) {
        setState(3)
      }
      else {
        default_change()
      }
    },
    (input) => {
      if (input !== 0) {
        setState(3)
      }
      else {
        default_change()
      }
    },
    default_change, default_change, end
  ]
  const next_page = (input) => () => {
    data[state] = input
    setData(data)
    states[state](input);
    // setState(state + 1);
    console.debug(data);
  }
  console.log(state);
  return (
    <div className={style.container}>
      <div>
        <h1 className={style.title}>安否登録</h1>
        <p className={style.text}>{titles[state]}</p>
      </div>

      <form action="" method="post">
        <div>
          <input
            className={style.safe}
            type="button"
            value={texts[state][0]}
            // value="安全です"
            onClick={next_page(1)}
          ></input>
        </div>
        <div>
          <input
            className={style.dangerous}
            type="button"
            value={texts[state][1]}
            // value="安全です"
            onClick={next_page(0)}
          ></input>
        </div>
      </form >

      <div className={style.img}>
        <div className={style.moveButton}>
          {state > 0 &&
            <a href="#" onClick={() => {
              for (let i = state - 1; i >= 0; i--) {
                if (data[i] !== undefined) {
                  setState(i)
                  break
                }
              }
            }}>
              <img src="./img/Left.png" width="100px"></img>
            </a>
          }
        </div>
        <h3>システムの状況</h3>
        <div className={style.moveButton}>
          {
            data[state] !== undefined &&
            <a href="#" onClick={() => states[state]()}>
              <img src="./img/Right.png" width="100px"></img>
            </a>
          }
        </div>
      </div>
      <hr className={style.hr}></hr>
    </div >
  );
};
export default situation;
