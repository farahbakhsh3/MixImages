import skimage as ski
import matplotlib.pyplot as plt

image_path = "../main.jpg"
image_data = ski.io.imread(image_path)[:, :, :3]

logo_path = "../2.jpg"
logo_data = ski.io.imread(logo_path)[:, :, :3]

a, b, c = logo_data.shape
ap, bp = 100, 100

if image_data.shape[0] < ap or image_data.shape[1] < bp:
    print("Error: logo width or height is bigger than main image width or height!")
else:
    for i in range(ap):
        for j in range(bp):
            logo_pixel = logo_data[
                int(i/ap*a),
                int(j/bp*b)
            ]

            if any(logo_pixel > 40):
                image_data[i, j] = logo_pixel

    ski.io.imsave("output.jpg", image_data)
    plt.imshow(image_data)
    plt.show()
