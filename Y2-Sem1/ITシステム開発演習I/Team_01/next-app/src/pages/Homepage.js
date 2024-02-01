import style from "../styles/homepage.module.css";
import movePage from "./_route.js";

export default function homepage() {
  return (
    <>
      <div className={style.hr}></div>
      <h1 className={style.companyName}>
        （会社の名前）
        <br />
        災害時連絡掲示板
      </h1>
      <div className={style.inputform}>
        <div>
          <label htmlFor="staffid">社員のID ：</label>
          <input
            className={style.inputText}
            type="text"
            name="staffid"
            id="staffid"
            required
          />
        </div>

        <div>
          <label htmlFor="password">暗証番号 ：</label>
          <input
            className={style.inputText}
            type="password"
            name="password"
            id="password"
            min="1"
            max="12"
            required
          />
        </div>
      </div>
      <a href="./situation1">
        <button type="submit" className={style.LoginSub}>
          登録
        </button>
      </a>
      <div className={style.hr}></div>
    </>
  );
}
