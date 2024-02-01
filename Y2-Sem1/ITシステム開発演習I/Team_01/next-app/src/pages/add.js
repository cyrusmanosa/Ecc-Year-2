import style from "../styles/addAnddel.module.css";
import movePage from "./_route.js";

export default function add() {
  return (
    <div className={style.container}>
      <div className={style.hr}></div>
      <h1 className={style.title}>追加</h1>
      <p className={style.text}>新社員の情報を教えてください。</p>

      <div className={style.inputform}>
        <div>
          <label htmlFor="staffName">社員の名前：</label>
          <input
            className={style.inputText}
            type="text"
            name="staffName"
            id="staffName"
            required
          />
        </div>

        <div>
          <label htmlFor="department">社員の部門：</label>
          <input
            className={style.inputText}
            type="text"
            name="department"
            id="department"
            required
          />
        </div>

        <a href="./addComplete">
          <div>
            <button type="submit" className={style.LoginSub}>
              追加確認
            </button>
          </div>
        </a>

        <div className={style.Cen}>
          <a href="./managiment">
            <img src="./img/Cen2.png" width={100} />
          </a>
        </div>

        <div className={style.footerPart}>
          <h3 className="footerWord">システムの状況:X</h3>
        </div>
      </div>
      <hr className={style.hr}></hr>
    </div>
  );
}
