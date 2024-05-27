import skimage as ski
import matplotlib.pyplot as plt
#image datas
img_path = "./main.jpg"
img_data = ski.io.imread(img_path)[:, :, :3]
#logo
lg_path = "./2.jpg"
lg_data = ski.io.imread(lg_path)[:, :, :3]
x,y,z = lg_data.shape
x1,x2=100,100

if img_data.shape[0] < x1 or img_data.shape[1] < x2:
    print("Er= Inconsistency in the size of the original photo logo")
else:
    for i in range(x1):
        for j in range(x2):
            lg_pix=lg_data[int(i/x1*x),int(j/x2*y)]
            if any(lg_pix>30):
                img_data[i,j] = lg_pix
    plt.imshow(img_data)
    plt.show()
