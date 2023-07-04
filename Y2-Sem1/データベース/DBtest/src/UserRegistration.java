//JCDB APIをインポートする
import java.sql.*;
import java.util.Scanner;
public class UserRegistration{
	public static void main(String[] args) throws Exception{
		System.out.println("～～～ユーザ登録処理～～～\n");

		//データベース接続に必要な変数を宣言
		Connection conn = null;
		Statement st = null;
		ResultSet rs = null;

		try{
			//スキャナーインスタンス化
			Scanner sc = new Scanner(System.in);
			//各項目の入力を行う
			System.out.print("名前を入力してください：");
			String uname = sc.nextLine();
			System.out.print("ふりがなを入力してください：");
			String ufname = sc.nextLine();
			System.out.print("メールアドレスを入力してください：");
			String email = sc.nextLine();
			System.out.print("パスワードを入力してください：");
			String password = sc.nextLine();
			System.out.print("電話番号を入力してください：");
			String tel = sc.nextLine();

			//カード番号は任意なので、質問により処理を分岐
			System.out.print("カード番号を登録しますか？ y「はい」、それ以外「いいえ」：");
			String cardans = sc.nextLine();
			String cardnum = "NULL";
			if (cardans.equals("y")) {
				System.out.print("カード番号を入力してください：");
				cardnum = sc.nextLine();
			}

			//お届け先は複数対応するので配列で管理
			String[] address = new String[9];
			String[] postnum = new String[9];
			int i = 0;
			System.out.print("郵便番号を入力してください：");
			postnum[i] = sc.nextLine();
			System.out.print("お届け先住所を入力してください：");
			address[i] = sc.nextLine();

			// 別のお届け先がある間、無限ループ
			while (true) {
				System.out.print("別のお届け先を登録しますか？ y「はい」、それ以外「いいえ」：");
				String addans = sc.nextLine();
				if (addans.equals("y")) {
					i++;
					System.out.print("郵便番号を入力してください：");
					postnum[i] = sc.nextLine();
					System.out.print("お届け先住所を入力してください：");
					address[i] = sc.nextLine();
				}else{
					break;
				}
			}
			System.out.println("～～～データベースに登録中～～～\n");
			
			//ドライバを読み込む(環境変数でCLASSPAHTの設定が必要)
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//データベース情報
			String dbname = "studbY2";   //接続データベース
			String dbuser = "dbuser";  //データベースユーザ
			String dbpass = "ecc";     //ログインパスワード

			//JDBCドライバ情報設定
			String dbinfo = "jdbc:mysql://localhost:3306/"+dbname+"?characterEncoding=UTF-8&serverTimezone=Asia/Tokyo";

			//データベースに接続する
			conn = DriverManager.getConnection(dbinfo, dbuser, dbpass);
			conn.setAutoCommit(false); //オートコミットを無効
			st = conn.createStatement();

			//Insert文を実行する(User表)
			String usersql  = "INSERT INTO USER (UNAME, RUBY, EMAIL, PASSWORD, TEL, CARD_NO) ";
			 	   usersql += "VALUES ('" + uname +"', '" + ufname + "', '" + email + "', '" + password +"','" + tel + "','" + cardnum + "' )";
			System.out.println(usersql);
			st.executeUpdate(usersql);

			//Insert文を実行する(Deliaddress表)
			String usersearch = "SELECT USER_NO FROM USER WHERE UNAME LIKE '%" + uname + "%'";
			rs = st.executeQuery(usersearch);

			String userno = null;
			while( rs.next() ){
				userno   = rs.getString("USER_NO");
				System.out.println(userno);
			}

			for (int j = 0; j <= i; j++) {
				String addresssql = "INSERT INTO Deliaddress (USER_NO, DELI_NO, POST_NO, ADDRESS) ";
				addresssql += "VALUES ('" + userno + "', '" + (j + 1) + "', '" + postnum[j] + "', '" + address[j] + "' )";
				System.out.println(addresssql);
				st.executeUpdate(addresssql);
			}

			//正常終了ならコミット
			conn.commit();
			System.out.println("コミットしました");
			System.out.println("～～～登録処理が完了しました～～～\n");

		}catch(Exception e){
			//エラーの場合は、ロールバックを行う。
			if(conn != null){
				System.out.println("～～～登録処理が異常終了しました～～～\n");
			}
			e.printStackTrace();
		}finally{
			//MySQLとの接続を切断する
			if(rs != null){ rs.close(); }
			if(st != null){ st.close(); }
			if(conn != null){ conn.close(); }
			
		}
	}
}
