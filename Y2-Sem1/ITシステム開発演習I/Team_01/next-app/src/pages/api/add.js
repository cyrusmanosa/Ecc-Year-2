export default function add() {
  return (
    <>
      <p className="title">メニュー</p>
      <div className="choose">
        <input
          type="button"
          value="社員状況一覧"
          className="allsitbtn"
          src="allsit.php"
        />
      </div>

      <div className="choose">
        <input type="button" value="管理" className="managebtn" />
      </div>
      <div className="choose">
        <input type="button" value="ログアウト" className="Logoutbtn" />
      </div>
    </>
  );
}
