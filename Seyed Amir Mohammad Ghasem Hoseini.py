import cv2
import numpy as np

# بارگذاری عکس اصلی و عکس پس‌زمینه
image = cv2.imread('main.jpg')
background = cv2.imread('2.jpg')

# تبدیل تصویر اصلی به فضای رنگ BGR
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# حذف پس‌زمینه با استفاده از تکنیک های پردازش تصویر
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# اعمال ماسک بر روی تصویر اصلی
image_fg = cv2.bitwise_and(image, image, mask=mask)

# اعمال ماسک معکوس بر روی پس‌زمینه
background_fg = cv2.bitwise_and(background, background, mask=mask_inv)

# ترکیب تصویر اصلی و پس‌زمینه
result = cv2.add(image_fg, background_fg)

# نمایش تصویر نهایی
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
