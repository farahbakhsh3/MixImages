import matplotlib.pyplot as plt
import skimage as ski

main_image = ski.io.imread('main.jpg')
logo_image = ski.io.imread('2.jpg')

logo_image[logo_image[:, :, :3] == 0] = 255

logo_resized = ski.util.img_as_ubyte(
    ski.transform.resize(logo_image[:, :, :3], (100, 100)))

main_image[:100, :100] = logo_resized

ski.io.imsave("image.jpg", main_image)
plt.imshow(main_image)
plt.show()
