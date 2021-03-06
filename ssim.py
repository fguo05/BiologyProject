from skimage.metrics import structural_similarity
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math


def ssim(total_num, step):
    ssim = []
    for i in range(0, total_num-step, step):
        print("=========" + str(i) + "=========")
        img1 = Image.open("./FruitingBodydata4/Early/Early_1/" + str(i + 1) + ".tif")
        img_arr1 = np.array(img1.getdata()).astype(float).reshape((1200, 1600))
        img2 = Image.open("./FruitingBodydata4/Early/Early_1/" + str(i + 1 + step) + ".tif")
        img_arr2 = np.array(img2.getdata()).astype(float).reshape((1200, 1600))
        ssim.append(structural_similarity(img_arr1, img_arr2))
    return np.array(ssim)


def psnr(total_num, step):
    psnr = []
    for i in range(0, total_num-step, step):
        print("=========" + str(i) + "=========")
        img1 = Image.open("./FruitingBodydata4/Early/Early_1/" + str(i + 1) + ".tif")
        img_arr1 = np.array(img1.getdata()).astype(float).reshape((1200, 1600))
        img2 = Image.open("./FruitingBodydata4/Early/Early_1/" + str(i + 1 + step) + ".tif")
        img_arr2 = np.array(img2.getdata()).astype(float).reshape((1200, 1600))
        mse = np.mean((img_arr1 - img_arr2) ** 2)
        if mse == 0:  # MSE is zero means no noise present in the signal.
            # Therefore PSNR has no importance.
            psnr.append(100)
            continue
        max_pixel = 255.0
        psnr.append(20 * math.log10(max_pixel / math.sqrt(mse)))
    return np.array(psnr)


ssim = ssim(1441, 2)
print(ssim)
plt.plot(ssim)
plt.title('ssim(step=1)')
plt.show()

# psnr = psnr(1441, 1)
# print(psnr)
# print(max(psnr), min(psnr))
# plt.plot(psnr)
# plt.title('psnr(step=1)')
# plt.show()
