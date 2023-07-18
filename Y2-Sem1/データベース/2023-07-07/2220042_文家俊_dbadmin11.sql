/*
データベース演習II 11週目
クラス：IE2A01
制作者：山田　太郎
作成日：2021/04/01
*/

/*
今回はMySQLでのバイナリログ形式によるレプリケーションを学習しました。
課題では、レプリケーションのパラメータの確認と、スレーブの解除を行います。
*/

-- 問１：レプリケーション状態を確認するコマンド「SHOW SLAVE STATUS\G」を
-- 実行して、以下のステータス情報を記載してください。
/*【回答】※内容は学生により変化します。
Slave_IO_State       ： Connecting to source
Master_Host          ： 10.200.1.110
Master_User          ： real
Master_Log_File      ： mysql-bin.000221
Read_Master_Log_Pos  ： 2115
Relay_Log_File       ： bingo.000221
Relay_Log_Pos        ： 2115
*/


-- 問２：スレーブ状態を停止してください。
   Stop slave;

-- 問３：スレーブ情報をリセットしてください。
   CHANGE MASTER TO ~

-- 問４：現在のバイナリログのファイル名とポジションを確認してください。

+---------------+----------+--------------+------------------+-------------------+
| File          | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+---------------+----------+--------------+------------------+-------------------+
| binlog.000021 |      157 |              |                  |                   |
+---------------+----------+--------------+------------------+-------------------+



-- 問５：レプリケーション状態を確認するコマンドを実行して、結果を記載してください。

*************************** 1. row ***************************
               Slave_IO_State: Connecting to source
                  Master_Host: 10.200.1.110
                  Master_User: repl
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000221
          Read_Master_Log_Pos: 2115
               Relay_Log_File: dbubuntu-relay-bin.000001
                Relay_Log_Pos: 4
        Relay_Master_Log_File: mysql-bin.000221
             Slave_IO_Running: Connecting
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 2115
              Relay_Log_Space: 157
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: NULL
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 2003
                Last_IO_Error: Error connecting to source 'repl@10.200.1.110:3306'. This was attempt 2/86400, with a delay of 60 seconds between attempts. Message: Can't connect to MySQL server on '10.200.1.110:3306' (110)
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 0
                  Master_UUID:
             Master_Info_File: mysql.slave_master_info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Replica has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp: 230707 05:23:04
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
       Master_public_key_path:
        Get_master_public_key: 0
            Network_Namespace:
1 row in set, 1 warning (0.01 sec)


