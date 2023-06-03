/*
データベース演習II 1週目
クラス：SK2A03
制作者：文家俊
作成日：2023/04/14
*/


/*
  今後の授業で、ピザ屋のデータベースを発展させていきます。
  その為にもSQL文を復習しながら、ピザ屋のデータベースの情報を整理しましょう。
*/

-- 問１：SHOW TABLES;でstudbに管理されているテーブルを表示してください。

Show tables;

-- 問２：店舗表(STORE)の全てのデータを取得してください。

Select * from store;

-- 問３：従業員表(EMPLOYEE)の全てのデータを取得してください。

Select * from employee;

-- 問４：従業員で給与が800円から850円の間の従業員を表示してください。

select name, salary from employee
where salary between '800' and '850';

-- 問５：商品表からピザの商品を税込み価格(10%)で表示をして下さい。

Select pname, price*1.1 as '税込み価格' from product Where category = 'ピザ';

-- 問６：従業員表から店舗ごとの平均給与を表示してください。

SELECT WORK_STORE , AVG(SALARY) FROM EMPLOYEE
GROUP BY WORK_STORE
ORDER BY WORK_STORE;

-- 問７：レシピ表と材料表からマルゲリータのレシピ情報を表示してください。

SELECT P.PNAME, M.MNAME, M.ORIGIN, R.QUANTITY FROM PRODUCT AS P
JOIN RECIPE AS R ON (P.PRODUCT_NO = R.PRODUCT_NO)
JOIN MATERIAL AS M ON (M.MATERIAL_NO = R.MATERIAL_NO)
WHERE P.PNAME = 'マルゲリータ';


-- 問８：レシピビュー(RECIPEVIEW)からBBQシーフードの情報を取得してください。

SELECT R.PRODUCT_NO, R.PNAME, M.MNAME, R.QUANTITY FROM recipeview as R
JOIN MATERIAL AS M on M.MNAME = R.MNAME
WHERE R.PNAME = 'BBQシーフード';







