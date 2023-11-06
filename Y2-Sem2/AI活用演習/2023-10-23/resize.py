# matplotlibとOpenCVをインポート
import matplotlib.pyplot as plt
import cv2

# 画像ファイルを読み込む
img = cv2.imread("./04_opencv_face/man.jpg")

# 画像のサイズを変更し、変更した画像をファイルに保存する
im2 = cv2.resize(img, (600, 300))
cv2.imwrite("./04_opencv_face/out-resize.png", im2)

# 変更した画像を表示する
plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()
