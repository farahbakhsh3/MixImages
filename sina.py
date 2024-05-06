import skimage as ski
import matplotlib.pyplot as plt

image_path = "./main.jpg"
image_data = ski.io.imread(image_path)

watermark_path = "./2.jpg"
watermark_data = ski.io.imread(watermark_path)


a, b, c = watermark_data.shape

ap, bp = 100, 100

if image_data.shape[0] < ap or image_data.shape[1] < bp:
    print("Error: could not add watermark!")
else:
    for i in range(ap):
        for j in range(bp):
            watermark_pixel = watermark_data[
                int(i/ap*a),
                int(j/bp*b)
            ]

            if any(watermark_pixel > 20):
                image_data[i, j] = watermark_pixel

    plt.imshow(image_data)
    plt.show()
