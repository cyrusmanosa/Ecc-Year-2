import style from "../styles/addAnddel.module.css";
import movePage from "./_route.js";

export default function del() {
  return (
    <div className={style.container}>
      <div className={style.hr}></div>
      <h1 className={style.title}>削除</h1>
      <p className={style.text}>社員の情報を教えてください。</p>

      <div className={style.inputform}>
        <div>
          <label htmlFor="staffName">社員 の ID ：</label>
          <input
            className={style.inputText}
            type="text"
            name="staffId"
            id="staffId"
            required
          />
        </div>

        <div>
          <label htmlFor="department">削除の理由：</label>
          <input
            className={style.inputText}
            type="text"
            name="reason"
            id="reason"
            required
          />
        </div>

        <a href="./delComplete">
          <div>
            <button type="submit" className={style.LoginSub}>
              削除確認
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
