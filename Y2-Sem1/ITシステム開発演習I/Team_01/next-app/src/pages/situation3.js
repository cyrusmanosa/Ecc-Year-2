import style from "../styles/situation.module.css";
import movePage from "./_route.js";
const situation3 = () => {
  return (
    <div className={style.container}>
      <div>
        <h1 className={style.title}>安否登録</h1>
        <p className={style.text}>周囲は安全ですか？</p>
      </div>

      <form action="" method="post">
        <div>
          <input
            className={style.safe}
            type="button"
            value="安全です"
            onClick={movePage("situation4")}
          ></input>
        </div>
        <div>
          <input
            className={style.dangerous}
            type="button"
            value="危険です"
            onClick={movePage("situation4")}
          ></input>
        </div>
      </form>

      <div className={style.img}>
        <a href="./situation2">
          <img src="../img/Left.png" width="100px"></img>
        </a>
        <h3>システムの状況:X</h3>
        <a href="./situation4">
          <img src="../img/Right.png" width="100px"></img>
        </a>
      </div>
      <hr className={style.hr}></hr>
    </div>
  );
};

export default situation3;
