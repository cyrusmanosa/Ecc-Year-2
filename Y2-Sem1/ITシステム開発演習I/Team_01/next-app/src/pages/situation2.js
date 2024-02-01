import style from "../styles/situation.module.css";
import movePage from "./_route.js";
const situation2 = () => {
  return (
    <div className={style.container}>
      <div>
        <h1 className={style.title}>安否登録</h1>
        <p className={style.text}>怪我をしていますか？</p>
      </div>

      <form action="" method="post">
        <div>
          <input
            className={style.safe}
            type="button"
            value="怪我無し"
            onClick={movePage("situation3")}
          ></input>
        </div>
        <div>
          <input
            className={style.dangerous}
            type="button"
            value="怪我有り"
            onClick={movePage("situation3")}
          ></input>
        </div>
      </form>

      <div className={style.img}>
        <div>
          <a href="./situation1">
            <img src="../img/Left.png" width="100px"></img>
          </a>
        </div>
        <h3>システムの状況:X</h3>
        <div>
          <a href="./situation3">
            <img src="../img/Right.png" width="100px"></img>
          </a>
        </div>
      </div>
      <hr className={style.hr}></hr>
    </div>
  );
};

export default situation2;
