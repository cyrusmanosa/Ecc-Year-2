# print("Hello ECC);
# name = "ECC"
# age = 22
# print(name)
# print(age)

# # print(f"名前：{name} 年齢：{age+100000}")

# # num = 1
# # # num = "1"
# # print(num * 2) # ←1が2回表示される

# # x,y,z = 1,2,3
# # print(x,y,z)

# # name = input("君の名は？>")
# # print(name + "さん、お待ちしておりました")

# # x = "321"
# # print(f"元の値{x}")
# # print(f"元のtype{type(x)}")
# # x = int(x) # int型に変換
# # print(f"変換後の値{x}")
# # print(f"変換後のtype{type(x)}")

# # point = [88,90,95]
# # print(point[0]) # 0番目を表示
# # print(point)    # 全要素を表示

# x = 1
# if x <= 1:
#     # trueの処理
#     print("ECC")
# elif x == 0:
#     print("aaa")
# else:
#     # falseの処理
#     print("computer")

# print("---------------")


def postTaxPrice(price):
    ans = int(price * 1.08)
    return ans


cost = postTaxPrice(120)
print(cost)