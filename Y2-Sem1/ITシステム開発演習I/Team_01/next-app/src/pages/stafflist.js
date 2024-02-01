import style from "../styles/stafflist.module.css";
import movePage from "./_route.js";

export default function stafflist() {
  return (
    <div className={style.container}>
      <div className={style.hr}></div>
      <h1 className={style.title}>社員状況一覧</h1>

      <table className={style.StaffList}>
          <tbody>
            <tr>
              <td>123</td>
              <td>123</td>
            </tr>
          </tbody>
      </table>

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
}
