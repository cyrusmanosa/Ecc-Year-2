import style from "../styles/management.module.css";
import movePage from "./_route.js";

const management = () => {
  return (
    <div className={style.container}>
      <div className={style.hr}></div>
      <div>
        <h1 className={style.title}>管理</h1>
      </div>

      <form action="" method="post">
        <div>
          <input
            className={style.delete}
            type="button"
            value="削除"
            onClick={movePage("del")}
          ></input>
        </div>
        <div>
          <input
            className={style.addition}
            type="button"
            value="追加"
            onClick={movePage("add")}
          ></input>
        </div>
      </form>

      <div className={style.Cen}>
            <a href="./completoin">
              <img src="./img/Cen2.png" width={100} />
            </a>
          </div>

          <div className={style.footerPart}>
            <h3 className="footerWord">システムの状況:X</h3>
          </div>
          <hr className={style.hr}></hr>
    </div>
  );
};

export default management;
