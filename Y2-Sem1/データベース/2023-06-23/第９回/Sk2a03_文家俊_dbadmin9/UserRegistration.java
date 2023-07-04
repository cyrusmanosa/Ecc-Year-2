//JCDB APIをインポートする
import java.sql.*;
import java.util.ArrayList;
import java.util.Scanner;

public class UserRegistration{
	
	public static void main(String[] args) throws Exception{
		System.out.println("～～～ユーザ登録処理～～～\n");
		//データベース接続に必要な変数を宣言
		Connection conn = null;
		Statement st = null;
		try{
			//スキャナーインスタンス化
			Scanner sc = new Scanner(System.in);
			
			//各項目の入力を行う
			System.out.print("名前を入力してください：");
			String uname = sc.nextLine();
			
			
			//カード番号は任意なので、質問により処理を分岐
			
			
			//お届け先は複数対応するので配列で管理
			
			
			
			// 別のお届け先がある間、無限ループ
			
			
			
			System.out.println("～～～データベースに登録中～～～\n");
			
			//ドライバを読み込む(環境変数でCLASSPAHTの設定が必要)
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//データベース情報
			
			
			
			//JDBCドライバ情報設定
			
			
			
			//データベースに接続する
			
			
			
			//Insert文を実行する(User表)
			
			
			
			//Insert文を実行する(Deliaddress表)
			
			
			
			//正常終了ならコミット
			
			
			
			System.out.println("～～～登録処理が完了しました～～～\n");
		}catch(Exception e){
			//エラーの場合は、ロールバックを行う。
			if(conn != null){
				System.out.println("～～～登録処理が異常終了しました～～～\n");
			}
			e.printStackTrace();
		}finally{
			//MySQLとの接続を切断する
			if(st != null){ st.close(); }
			if(conn != null){ conn.close(); }
			
		}
	}
}
