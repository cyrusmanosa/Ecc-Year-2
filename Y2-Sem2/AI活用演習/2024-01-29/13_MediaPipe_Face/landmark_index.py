import cv2
import mediapipe as mp

try:
    # MediaPipe Face Meshの初期化
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    # MediaPipe描画ユーティリティの初期化
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)


    # 読み込む画像ファイルのパス
    image_path = './face_sample.png'

    # 画像を読み込む
    image = cv2.imread(image_path)
    if image is None:
        print("Image could not be loaded.")  # 画像が読み込めない場合のエラーメッセージ
    else:

        # イメージをMediaPipeで処理
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        # イメージをBGRに戻す
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        # 顔のランドマークを描画
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    landmark_drawing_spec=drawing_spec
                )

                # 各ランドマークのインデックスを描画
                for idx, landmark in enumerate(face_landmarks.landmark):
                    ih, iw, _ = image.shape
                    x, y = int(landmark.x * iw), int(landmark.y * ih)
                    cv2.putText(image, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

        # 画像をウィンドウに表示
        cv2.imshow('MediaPipe FaceMesh', image)
        cv2.waitKey(0)                   # キーが押されるまでウィンドウを表示
        cv2.destroyAllWindows()          # ウィンドウを閉じる
except Exception as e:
    print(f"エラーが発生しました: {e}")   # エラーが発生した場合のエラーメッセージ