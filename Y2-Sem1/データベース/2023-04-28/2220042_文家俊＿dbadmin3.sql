/*
データベース演習II 3週目
クラス：SK2A03
制作者：文家俊
作成日：2023/04/28
*/

/*
今回は、接続元の設定とユーザの権限を管理することでセキュリティの向上について学習をしました。
課題では、dbuserのセキュリティを上げると共に、外部から接続できるユーザのセキュリティを
考慮して作成していきます。
*/

--問１：dbuserをlocalhostからのみMySQLに接続できるようにしてください。

RENAME USER dbuser TO dbuser@localhost;
SELECT USER,HOST FROM MYSQL.USER WHERE USER='dbuser';

--問２：どの接続元からアクセスできるdbshowユーザを作成してください。

CREATE USER dbshow
IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY 'ecc';
SELECT USER,HOST FROM MYSQL.USER WHERE USER='dbshow';

--問３：dbshowは外部からアクセスできるため、データの検索のみ許可します。
--      studbデータベースに対してSELECT権限を付与してください。

GRANT USAGE ON *.* TO dbshow;
GRANT SELECT ON studbY2.* TO dbshow;
SHOW GRANTS FOR dbshow;

--問４：dbshowユーザでログインして、商品名にサラダが含まれている商品を
--      表示してください。

SELECT * FROM PRODUCT WHERE PNAME LIKE '%サラダ';

--問５：dbshowユーザでシーザーサラダの商品価格を500に更新を試してください。

UPDATE product SET PRICE = '500' WHERE PNAME = ‘シーザーサラダ’;
SELECT * FROM product WHERE pname = ‘シーザーサラダ’;

--問６：dbtestユーザに商品表の検索、挿入、更新、削除権限を付与してください。

GRANT SELECT,INSERT,UPDATE,DELETE ON studbY2.product TO dbtest@localhost;
SHOW GRANTS FOR dbtest@localhost;

--問７：dbtestユーザでシーザーサラダの商品価格を500に更新してください。
--      データ確認後、トランザクションを取り消してください。

UPDATE PRODUCT SET PRICE = 500 WHERE PNAME = 'シーザーサラダ';
SELECT * FROM product WHERE PNAME LIKE '%サラダ';

Rollback;


/*
ハンズオンでRootユーザのパスワードを変更しました。
Rootパスワードのリセット方法で元のパスワードに変更します。
*/


--問８：設定ファイルを編集して、認証の無効化をしてください。
--      変更したオプションを回答してください。
/*
設定オプション： MACですから。。。。。。
*/


--問９：rootユーザのパスワードをrootに変更してください。

alter user 'root'@'localhost' identified by 'root';
set password for root@localhost = 'root';



--問１０：設定ファイルを編集して、認証の有効化をしてください。
--        変更したオプションを回答してください。
/*
設定オプション：MACですから。。。。。。
*/


