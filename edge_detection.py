# %% [markdown]
# <a href="https://colab.research.google.com/github/ShibleNK/is-cv/blob/main/edge_detection.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %% [markdown]
# # Sobel Edge Detection
# 

# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Load the image

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error loading image")
    exit()


# Apply Gaussian smoothing (optional)
blurred_image = cv2.GaussianBlur(image, (3,3),0)

# Sobel operators
Gx = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
Gy = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

# Gradient magnitude
sobel = np.sqrt(Gx**2 + Gy**2)

# Normalize to range 0-255
Gx = np.uint8(255 * np.abs(Gx) / np.max(Gx))
Gy = np.uint8(255 * np.abs(Gy)/ np.max(Gy))
sobel = np.uint8(255 * sobel / np.max(sobel))

# Display the results
plt.figure(figsize=(15,10))

# Original image
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Gradient in X direction
plt.subplot(2,2,2)
plt.imshow(Gx, cmap='gray')
plt.title('Gradient in X direction')
plt.axis('off')

# Gradient in Y direction
plt.subplot(2,2,3)
plt.imshow(Gy, cmap='gray')
plt.title('Gradient in Y direction')
plt.axis('off')

# Edge-detected image
plt.subplot(2,2,4)
plt.imshow(sobel, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')

plt.show()

# %% [markdown]
# # Canny Edge Detection

# %%
# Load the image

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(image,(5,5), 1.4)

# Apply Canny edge detector
edges = cv2.Canny(blurred_image, 100, 200)

# Display the result
plt.figure(figsize=(10,5))

# Original image
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Edge-detected image

plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')

plt.show()


