import cv2                             # OpenCVライブラリをインポート
import mediapipe as mp                 # MediaPipeライブラリをインポート

try:
    # MediaPipeのFace Meshモデルを初期化
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    # MediaPipeの描画ユーティリティを初期化
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)  # 描画の設定（線の太さ、円の半径）
    
    # 読み込む画像ファイルのパス
    image_path = 'baby.jpg'

    # 画像を読み込む
    image = cv2.imread(image_path)
    if image is None:
        print("Image could not be loaded.")  # 画像が読み込めない場合のエラーメッセージ
    else:
        # 画像をRGB形式に変換（MediaPipeはBGRではなくRGBで処理する）
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Face Meshモデルで画像を処理
        results = face_mesh.process(image_rgb)
        
        # 画像をBGR形式に戻す（OpenCVの表示に使用）
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        
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
        cv2.waitKey(0)                   # キーが押されるまでウィンドウを表示
        cv2.destroyAllWindows()          # ウィンドウを閉じる


    
except Exception as e:
    print(f"エラーが発生しました: {e}")   # エラーが発生した場合のエラーメッセージ
