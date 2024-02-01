import style from "../styles/situation.module.css";
import movePage from "./_route.js";

const delComplete = () => {
  return (
    <>
      <div className={style.container}>
        <div>
          <h1 classNaem={style.title}>削除</h1>
        </div>

        <div className={style.inputform}>
          <div>
            <h2 className={style.text}>社員 : (社員のID) 削除しました</h2>
          </div>

          <div className={style.Cen}>
            <a href="./completoin">
              <img src="./img/Cen2.png" width={100} />
            </a>
          </div>

          <div className={style.footerPart}>
            <h3 className="footerWord">システムの状況:X</h3>
          </div>
        </div>
        <hr className={style.hr}></hr>
      </div>
    </>
  );
};
export default delComplete;
