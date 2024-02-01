import cv2                              # OpenCVライブラリをインポート
import mediapipe as mp                  # MediaPipeライブラリをインポート

try:
    # MediaPipe Face Meshの初期化
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()
    
    # MediaPipe描画ユーティリティの初期化
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1) # 描画の設定（線の太さ、円の半径）
    
    # カメラのキャプチャを開始（0は内蔵カメラを指す）
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # カメラの幅を640に設定
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # カメラの高さを480に設定
    
    while cap.isOpened():                   # カメラがオープンしている間
        # カメラから画像を読み込む
        success, image = cap.read()         
        if not success:
            print("Ignoring empty camera frame.") # エラーメッセージ
            continue
        
        # 画像をRGB形式に変換
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Face Meshモデルで画像を処理
        results = face_mesh.process(image)
        
        # 画像をBGR形式に戻す
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # 顔のランドマークが検出された場合
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 顔のランドマークを描画
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    landmark_drawing_spec=drawing_spec
                )
        
        # 画像をウィンドウに表示
        cv2.imshow('MediaPipe FaceMesh', image)
        
        # 'q' キーが押されたらループから出てプログラムを終了
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        
except Exception as e:
    print(f"エラーが発生しました: {e}")   # エラーが発生した場合のメッセージ
finally:
    # リソースを解放するためのクリーンアップ処理
    cap.release()                         # カメラのキャプチャをリリース
    cv2.destroyAllWindows()               # ウィンドウを閉じる
