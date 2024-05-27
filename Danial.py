import skimage as ski
from skimage import transform as tf
import matplotlib.pyplot as plt

logo = ski.io.imread('./2.jpg')
image = ski.io.imread('./main.jpg')

tform = tf.SimilarityTransform()
logo_warped = tf.warp(logo, tform.inverse)

result = image.copy()
result[:logo_warped.shape[0], :logo_warped.shape[1]
       ] = ski.util.img_as_ubyte(logo_warped)

plt.imshow(result, cmap='gray')
plt.show()
