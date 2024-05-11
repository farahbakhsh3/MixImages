import numpy as np
from skimage import io, color
from skimage.filters import threshold_otsu

def remove_black_background(logo):
    logo_gray = color.rgb2gray(logo)
    thresh = threshold_otsu(logo_gray)
    mask = logo_gray < thresh
    alpha = np.where(mask, 0, 255).astype(np.uint8)
    logo_rgba = np.dstack((logo[:, :, :3], alpha))
    return logo_rgba

def process_images(main_image_path, logo_path, output_path):
    main_image = io.imread(main_image_path)
    logo = io.imread(logo_path)
    
    logo_rgba = remove_black_background(logo)
    
    for y in range(logo_rgba.shape[0]):
        for x in range(logo_rgba.shape[1]):
            if logo_rgba[y, x, 3] > 0:  
                main_image[y, x] = logo_rgba[y, x, :3] 

    io.imsave(output_path, main_image)

process_images('main.jpg', '2.jpg', 'combined_photo.png')
