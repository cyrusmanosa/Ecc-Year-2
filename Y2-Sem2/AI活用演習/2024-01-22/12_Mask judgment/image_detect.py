import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
# 学習済みモデルのロード
model = load_model('./mask_model.keras') # 保存されたモデルのパスを指定


# 画像のロードと前処理
# 画像の読み込みと前処理
IMG_SIZE = 224
image_path = './no_mask_sample.png' # 判定したい画像のパス
image = load_img(image_path, target_size=(IMG_SIZE , IMG_SIZE )) # 画像のリサイズ
image_array = img_to_array(image) # 画像を配列に変換
image_preprocessed = image_array / 255.0 # ピクセル値の正規化
image_preprocessed = np.expand_dims(image_preprocessed, axis=0) # バッチの次元を追加


# 予測
predictions = model.predict(image_preprocessed)
predicted_class = np.argmax(predictions)


# 結果の表示
plt.imshow(image_array.astype('uint8'))
plt.axis('off') # 軸を非表示に

if predicted_class == 0:
    plt.title("wear_mask")
else:
    plt.title("no_mask")

plt.show()