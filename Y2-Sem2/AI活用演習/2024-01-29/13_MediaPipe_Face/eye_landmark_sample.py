import cv2  # OpenCVライブラリをインポート
import mediapipe as mp  # MediaPipeライブラリをインポート

try:
    # MediaPipe Face Meshの初期化
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()
    
    # カメラの設定（0は内蔵カメラを指す）
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # カメラの幅を640に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # カメラの高さを480に設定
    
    if not cap.isOpened():
        print("カメラが見つかりません。")  # カメラが見つからないときのエラーメッセージ
        exit()
    
    while True:  # カメラからの映像を無限ループで処理
        success, image = cap.read()
        if not success:
            print("カメラから画像を取得できませんでした。")  # 画像が読み込めない場合のエラーメッセージ
            break

        # 画像をRGB形式に変換
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # 顔のランドマークを検出
        results = face_mesh.process(image)
        
        # 画像をBGR形式に戻す
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # 顔のランドマークが検出された場合
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 左目と右目のランドマーク インデックスを定義(左、上、右、下)
                left_eye_indices = [33, 159, 173 , 145]
                right_eye_indices = [398 , 388 , 466 , 374]
        
                # 左目と右目の中心座標を計算
                left_eye_x = sum(face_landmarks.landmark[i].x for i in left_eye_indices) / len(left_eye_indices)
                left_eye_y = sum(face_landmarks.landmark[i].y for i in left_eye_indices) / len(left_eye_indices)
                right_eye_x = sum(face_landmarks.landmark[i].x for i in right_eye_indices) / len(right_eye_indices)
                right_eye_y = sum(face_landmarks.landmark[i].y for i in right_eye_indices) / len(right_eye_indices)

                # 画面上の座標に変換
                ih, iw, _ = image.shape
                left_eye_x, left_eye_y = int(left_eye_x * iw), int(left_eye_y * ih)
                right_eye_x, right_eye_y = int(right_eye_x * iw), int(right_eye_y * ih)

                # 目の中心に緑色の円を描く
                cv2.circle(image, (left_eye_x, left_eye_y), 5, (0, 255, 0), -1)
                cv2.circle(image, (right_eye_x, right_eye_y), 5, (0, 255, 0), -1)

        # 画像をウィンドウに表示
        cv2.imshow('MediaPipe FaceMesh', image)

        # 'q' キーが押されたらプログラムを終了
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        
except Exception as e:
    print(f"エラーが発生しました: {e}")  # エラーが発生した場合のメッセージ

finally:
    # プログラム終了時にリソースを解放
    cap.release()  # カメラのキャプチャをリリース
    cv2.destroyAllWindows()  # ウィンドウを閉じる
