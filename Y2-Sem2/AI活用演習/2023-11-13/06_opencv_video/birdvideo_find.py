# 必要なライブラリを読み込む
import cv2 # 画像処理ライブラリ
import os # ファイルシステム操作用ライブラリ
import copy # リストのコピー用ライブラリ
import pickle # Pythonオブジェクトの直列化/逆直列化用ライブラリ

# 学習済みモデルを読み込む
with open("bird.pkl", "rb") as fp:
    model = pickle.load(fp)

# 出力先ディレクトリの設定
output_dir = "./bestshot"
if not os.path.isdir(output_dir):  # ディレクトリが存在しなければ作成
    os.mkdir(output_dir)

""" 変数の初期化 """
img_last = None  # 前回の画像
bird_th = 10  # 鳥の検出数の閾値
count = 0  # 鳥が検出されたフレームの数
frame_count = 0  # フレームの総数

# 動画ファイルの読み込み
cap = cv2.VideoCapture("bird.mp4")

# 動画のフレームを1つずつ処理するループ
while True:
    
    # 動画のフレームを読み込む
    res , frame = cap.read()
    
    # フレームが読み込めなくなったらループを抜ける
    if not res : break
    
    # フレームのサイズをリサイズする
    frame = cv2.resize(frame, (640, 360))

    # フレームのコピーを作成する
    frame_cp = copy.copy(frame)

    # フレーム数をカウントする
    frame_count += 1

    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 画像にガウシアンフィルタを適用する
    gray = cv2.GaussianBlur(gray, (9, 9), 0)

    # 二値化する
    img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    # 前回のフレームとの差分を計算する
    if not img_last is None:
        # 前フレームと比較して、現在のフレームで動いたもの（変化した部分）を検出する
        frame_diff = cv2.absdiff(img_last,img_b)

        # 変化した部分を輪郭抽出する
        cnts = cv2.findContours(frame_diff,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

        """ バウンディングボックスを描きながら、検出した領域が鳥かどうか判定する """
        # 鳥と判定された領域の数を初期化する
        bird_count = 0
        
        # すべての検出された輪郭について繰り返す
        for pt in cnts:  
            # 輪郭のバウンディングボックスの座標を取得する
            x, y, w, h = cv2.boundingRect(pt)  
            
            # バウンディングボックスの幅が30未満または300を超える場合は、スキップする
            if w < 30 or w > 300:  
                continue
            
            # バウンディングボックスの領域を切り抜く
            img_box = frame[y:y+h, x:x+w]
            
            # 切り抜いた領域を64x32にリサイズする
            img_resize = cv2.resize(img_box, (64, 32))
            
            # 画像データを1次元配列に変換する
            img_data = img_resize.reshape(-1,)
            
            # モデルで鳥かどうかを予測する
            pred_y = model.predict([img_data])
            
            # 鳥と予測された場合
            if pred_y[0] == 1:  
                
                # 鳥の数をカウントする
                bird_count += 1
                
                # バウンディングボックスを緑色で描画する
                cv2.rectangle(frame_cp, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                """ 鳥と判定された領域が一定数以上あれば、フレームを保存する """
                # もし鳥と判定された領域の数が、あらかじめ指定された鳥の閾値を超えた場合
                if bird_count > bird_th:  
                    
                    # ファイル名を設定する
                    bname = f"{output_dir}/bird{str(count)}.png"
                    
                    # フレームをファイルに保存する
                    cv2.imwrite(bname, frame)
                    
                    # 鳥と判定されたフレーム数をカウントする
                    count += 1

    # 現在のフレームを画面に表示する
    cv2.imshow("Bird!",frame_cp)

    # Escキーが押されると、処理を中止する
    if cv2.waitKey(1) == 27:
        break

    # 前フレームを更新する
    img_last = img_b

""" メモリの解放と処理結果の表示 """
# 動画キャプチャを解放する
cap.release()

# すべてのウィンドウを閉じる
cv2.destroyAllWindows()  
# 鳥と判定されたフレーム数と総フレーム数を表示する
print(f"OK {count} \\ {frame_count}")