# 必要なライブラリをインポートします
import cv2
import mediapipe as mp

# mediapipeから描画用ユーティリティと、手検出のソリューションを読み込みます
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands



# ウェブカメラからの入力を設定します（0は一番目のカメラを指します）
cap = cv2.VideoCapture(1)


# 手の検出を行うオブジェクトを作成します
# 最低限の検出信頼度と追跡信頼度はそれぞれ0.5（50%）に設定
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    # カメラが開いている限り処理を続けます
    while cap.isOpened():
        # カメラから画像を一枚読み込みます
        success, image = cap.read()

        # 画像が読み込めなかった場合は処理をスキップします
        if not success:
            print("カメラから画像が取得できませんでした")
            continue
        
        # 画像を左右反転させ、BGR形式からRGB形式に変換します（mediapipeはRGB形式を前提としています）
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        

        # 画像の書き込みを無効にすることで、パフォーマンスを向上させます
        image.flags.writeable = False
        
        # 手の検出を行います
        results = hands.process(image)

        # 画像の書き込みを再度有効にし、RGB形式からBGR形式に戻します（OpenCVはBGR形式を前提としています）
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        


        # 手が検出された場合
        if results.multi_hand_landmarks:
            # 検出されたすべての手について
            for hand_landmarks in results.multi_hand_landmarks:
                # 手のランドマーク（指の関節部分など）と、それらをつなぐ線を描画します
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)


        # 描画結果の画像を表示します
        cv2.imshow('MediaPipe Hands', image)

        # 'q'キーで終了
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# カメラを閉じます
cap.release()
