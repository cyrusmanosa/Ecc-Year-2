//JCDB APIをインポートする
import java.sql.*;

public class MySQLConnect{

    public static void main(String[] args) throws Exception{

        System.out.println("MySQL接続プログラム開始\n");
		
		//データベース接続に必要な変数を宣言
        Connection conn = null;
        Statement st = null;
        ResultSet rs = null;

        try{
            //ドライバを読み込む(環境変数でCLASSPAHTの設定が必要)
            Class.forName("com.mysql.cj.jdbc.Driver");

            //データベース情報
            String dbname = "studb";   //接続データベース
            String dbuser = "dbuser";  //データベースユーザ
            String dbpass = "ecc";     //ログインパスワード

            //JDBCドライバ情報設定
            String dbinfo = 
                "jdbc:mysql://localhost/"+dbname+"?characterEncoding=UTF-8&serverTimezone=JST";

            //データベースに接続する
            conn = DriverManager.getConnection(dbinfo, dbuser, dbpass);
			conn.setAutoCommit(false); //オートコミットを無効
			
            st = conn.createStatement();
			
			//INSERT文を作成する
			String isql  = "INSERT INTO product (product_no, pname, category, price ) ";
			       isql += "VALUES ('1015', 'バナナアイス', 'サイド', 370 )";
			
			//SQL文を出力しておく
		    System.out.println(isql); 
			
			//executeUpdate関数でUPDATE、INSERTまたは、CREATEなどのDDL文が実行できる。
			//戻り値は、データ処理件数
			int cnt = st.executeUpdate(isql);
            System.out.println(cnt +"件のデータを登録しました\n");
			
			
            //SELECT文を送信する
            String ssql = "SELECT * FROM product WHERE pname LIKE '%アイス%'";
			//SQL文を出力しておく
		    System.out.println(ssql); 

            //SELECT文の場合は、executeQuery関数を使用する。
			//こちらは実行結果が戻り値になるので結果をデータセットに格納する
            rs = st.executeQuery(ssql);

            //データベースの値を受け取る変数宣言
            String productNo;
            String productName;
            String category;
            int price;
			
            //データセットにデータが存在する間繰り返す
            while(rs.next()){

                productNo   = rs.getString("PRODUCT_NO");
                productName = rs.getString("PNAME");
                category    = rs.getString("CATEGORY");
                price       = rs.getInt("PRICE");

                // １行ごとに商品情報を画面に出力する
                String wkSt = "商品番号："+ productNo +
                              " 商品名："+ productName +
                              " カテゴリ："+ category +
                              " 価格：" + price ;
                System.out.println(wkSt);
            }
			
			//ハンズオンの為、ロールバックを行う。
			conn.rollback();
		    System.out.println("\nロールバックしました"); 


        }catch(Exception e){
			
			//エラーの場合は、ロールバックを行う。
			if(conn != null){
				conn.rollback();
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

