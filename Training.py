
import skimage as ski
import numpy as np
import matplotlib.pyplot as plt
file_path = "C:/Users/zgb-02/Desktop/main.jpg"
file_data = ski.io.imread(file_path)[:, :, :3]
file2_path = "C:/Users/zgb-02/Desktop/2.jpg"
file2_data = ski.io.imread(file2_path)[:, :, :3]
num1, num2, num3 = file2_data.shape
ap, bp = 200,200

new_logo = np.zeros((ap,bp,num3), dtype=np.uint8)

if file_data.shape[0] < ap or file_data.shape[1] < bp:
    print("Size Problem")
else:
    for i in range(ap):
        for j in range(bp):
            logo_pixel = file2_data[
                int(i/ap*num1),
                int(j/bp*num2)
            ]
            
            if any(logo_pixel > 40):
                new_logo[i,j] = logo_pixel
            else:
                new_logo[i,j] = (255,255,255)
                
    file_data[:ap, :bp, :num3] = new_logo
            
    plt.imshow(file_data)
    plt.show()