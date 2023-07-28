/*
データベース演習II 13週目
クラス：SK2A03
制作者：文家俊
作成日：2023/07/21
*/

/*
  トリガーを使うことで、特定の動作に対して自動的にSQLを実行することが出来るようになりました。
  課題では、車体管理表を削除した時に自動的に廃車表に登録を行うTRI_BIKEトリガーの作成を行います。
*/

-- 問１：以下の列構造を持つ、廃車表を作成してください。


CREATE TABLE SCRAPBIKE (
 DELDATE DATE,
 BIKE_NO CHAR(5),
 STORE_NO CHAR(3)
);


-- 問２：以下の発動条件と処理を行うTRI_BIKEトリガーを作成してください。


DELIMITER //
CREATE TRIGGER TRI_BIKE BEFORE DELETE
ON BIKE FOR EACH ROW
BEGIN

  IF OLD.BIKE_NO IS NOT NULL THEN
    INSERT INTO SCRAPBIKE (DELDATE, BIKE_NO, STORE_NO)
    VALUES (NOW(), OLD.BIKE_NO, OLD.STORE_NO);
  END IF;

END //
DELIMITER ;


-- 問３：車両番号「00001」のスーパーカブ 50 プロのデータを削除してください。


DELETE FROM BIKE WHERE BIKE_NO = 00001;


-- 問４：廃車表のデータを確認してください。


SELECT * FROM SCRAPBIKE;


-- 問５：トランザクションの確定をして下さい。


Commit;


/*
  カーソルを使うことで、複数件のデータに対して１件ずつ処理を行うことが出来るようになりました。
  現在、ピザの商品一覧には原材料の原価合計より安く設定されている商品があります。
  そこで、カーソルを利用したプロシージャを作成して価格の再設定を行います。
*/

-- 問６：カテゴリーがピザの商品情報を表示してください。


SELECT * FROM PRODUCT WHERE CATEGORY = 'ピザ';


-- 問７：カテゴリーがピザである商品ごとの原価合計を表示してください。


SELECT p.PRODUCT_NO, SUM(r.QUANTITY * m.COST)
FROM PRODUCT AS p
JOIN RECIPE AS r ON r.PRODUCT_NO = p.PRODUCT_NO
JOIN MATERIAL AS m ON m.MATERIAL_NO = r.MATERIAL_NO
WHERE p.CATEGORY = 'ピザ'
GROUP BY p.PRODUCT_NO;


-- 問８：以下の仕様に従い、商品一覧の中で原価より安い価格を値上げするPIZZA_PRICEUPプロシージャを作成してください。


DELIMITER //
CREATE PROCEDURE PIZZA_PRICEUP()
BEGIN

 DECLARE WK_PRODUCT_NO CHAR(4);
 DECLARE WK_PRICE INT;
 DECLARE WK_PRO_COST INT;
 DECLARE done INT DEFAULT FALSE;

 DECLARE cur CURSOR FOR
  SELECT PRODUCT_NO,PRICE FROM PRODUCT WHERE CATEGORY='ピザ';
 DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

 OPEN cur;
 WHILE NOT done DO
  FETCH cur INTO WK_PRODUCT_NO,WK_PRICE;

   SELECT FLOOR(SUM(r.QUANTITY * m.COST)/100)*100 INTO WK_PRO_COST
   FROM PRODUCT AS p
   JOIN RECIPE AS r ON r.PRODUCT_NO = p.PRODUCT_NO
   JOIN MATERIAL AS m ON m.MATERIAL_NO = r.MATERIAL_NO
   WHERE p.CATEGORY = 'ピザ' AND p.PRODUCT_NO = WK_PRODUCT_NO
   GROUP BY p.PRODUCT_NO;

   IF WK_PRICE < WK_PRO_COST THEN
    UPDATE PRODUCT
    SET PRICE = WK_PRO_COST + 200
    WHERE PRODUCT_NO = WK_PRODUCT_NO;
   END IF;

 END WHILE;
 CLOSE cur;

END //
DELIMITER ;


-- 問９：PIZZA_PRICEUPプロシージャを実行してください。


CALL PIZZA_PRICEUP();


-- 問１０：カテゴリーがピザの商品情報を表示してください。


SELECT * FROM PRODUCT WHERE CATEGORY = 'ピザ';


-- 問１１：トランザクションの確定をして下さい。


Commit;



