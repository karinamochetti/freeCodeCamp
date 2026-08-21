def mix_paint(bucket1, bucket2):
    f1 = bucket1["fullness"]
    f2 = bucket2["fullness"]
    f = f1+f2
    f1 = f1 / f
    f2 = f2 / f

    return [round(bucket1["color"][i]*f1 + bucket2["color"][i]*f2) for i in range(3)]

    
print(mix_paint({"color": [250, 250, 250], "fullness": 50}, {"color": [0, 0, 0], "fullness": 50}))
print(mix_paint({"color": [250, 250, 250], "fullness": 80}, {"color": [0, 0, 0], "fullness": 20}))
print(mix_paint({"color": [100, 150, 200], "fullness": 30}, {"color": [100, 150, 200], "fullness": 70}))
print(mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90}))
print(mix_paint({"color": [15, 134, 249], "fullness": 29}, {"color": [97, 178, 55], "fullness": 54}))
