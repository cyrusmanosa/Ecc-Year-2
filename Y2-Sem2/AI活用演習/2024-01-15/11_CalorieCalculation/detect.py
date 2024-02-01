# 必要なライブラリのインポート
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
from matplotlib import rcParams

# matplotlibの設定を変更して、日本語が正しく表示されるようにします。
rcParams['font.sans-serif'] = "YuGothic"
rcParams['font.family'] = "YuGothic"

# 学習済みのモデルを読み込みます。
model = load_model('my_model.keras') 

# 予測結果に対応するカテゴリ名とカロリーをリストで定義します。
class_names = ['寿司', 'サラダ', 'とんかつ'] #予測結果の文字列
class_calories = [588, 118,1000] #予測結果のカロリー配列

# 予測を行いたい画像のファイルパスを設定します。
img_paths = ['./Sushi-1-1.jpg', './a3333.jpg', './a000037.jpg']

# 画像の読み込みと前処理を行います。
images = []
for img_path in img_paths:
    img = image.load_img(img_path, target_size=(128, 128)).convert("RGB")
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x.astype('float32') / 255.0
    images.append(x)

# 予測結果を画像とともに表示します。
fig, axs = plt.subplots(1, len(img_paths), figsize=(12, 4))

for i in range(len(img_paths)):
    # モデルを使って予測を行います。
    predictions = model.predict(images[i])
    predicted_class = np.argmax(predictions[0])

    predict_text = '\n'.join([f"{class_names[i]} = {int(acc * 100)}%" for i, acc in enumerate(predictions[0])])
    predict_text += f'\nこの画像は、おそらく:{class_names[predicted_class]}, カロリーは:{class_calories[predicted_class]} kcal'

    axs[i].imshow(images[i][0])
    axs[i].set_title(predict_text)
    axs[i].axis('off')
    print(predict_text)

plt.show()

