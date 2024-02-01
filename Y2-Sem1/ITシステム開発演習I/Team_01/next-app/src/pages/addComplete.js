import style from "../styles/situation.module.css";
import movePage from "./_route.js";

export default function addComplete() {
  return (
    <>
      <div className={style.container}>
        <div>
          <h1 className={style.title}>追加</h1>
        </div>

        <div className={style.inputform}>
          <div className={style.text}>
            <h2> 社員 : 社員のID追加できました</h2>
            <h2>ありがとうございました！</h2>
          </div>

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
      </div>
    </>
  );
}
