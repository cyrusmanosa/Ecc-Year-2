import matplotlib.pyplot as plt
import cv2

# Haar-cascade分類器を読み込む
cascade_file = "./haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

# 画像を読み込み、グレースケールに変換する
img = cv2.imread("./04_opencv_face/baby.png")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Haar-cascade分類器を用いて顔を検出する
face_list = cascade.detectMultiScale(img_gray,minSize=(150,150))

# 顔が検出されなかった場合はプログラムを終了する
if len(face_list) == 0:
    print("顔が見つかりません")
    quit()

# 検出された顔の数だけ処理する
for(x,y,w,h) in face_list:
    # 顔の座標を出力する
    print("顔の座標=",x,y,w,h)
    # 赤色の線で顔の周りに四角形を描画する
    red = (0,0,255)
    cv2.rectangle(img , (x,y) , (x+w , y+h) , red , thickness=20)

# 処理された画像を保存する
cv2.imwrite("./04_opencv_face/face-detect.png",img)

# 画像を表示する
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()