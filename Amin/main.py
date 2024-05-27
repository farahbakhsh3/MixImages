from PIL import Image

# Load the original image
original_image = Image.open("original_image.jpg")

# Load the logo image
logo_image = Image.open("logo_image.png")

# Resize the logo image to 100x100 pixels
logo_image = logo_image.resize((100, 100))

# Remove the background from the logo image (assuming the background is white)
logo_image = logo_image.convert("RGBA")
data = logo_image.getdata()

new_data = []
for item in data:
    if item[:3] == (0, 0, 0):
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

logo_image.putdata(new_data)

# Paste the logo image on the original image at the top left corner
original_image.paste(logo_image, (0, 0))

# Save the modified image
original_image.save("modified_image.jpg")
