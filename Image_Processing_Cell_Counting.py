import matplotlib
import numpy as np
import cv2
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  #I put that code to fix a problem with my matplotlib library so if you encounter with a problem try to remove that part of the code

#Method 1: Hough
#Loading cells image
gray = cv2.imread('C:/Users/emree/Downloads/images (1)/images/cells.png', 0)
#Preprocessing - Gaussian Blur
blurred = cv2.GaussianBlur(gray, (9, 9), 2)
#Hough Circle Detection
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=15,
    param1=50,
    param2=20,
    minRadius=10,
    maxRadius=30
)
#Output for hough method
output = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
hough_count = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    hough_count = len(circles[0])
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2) # Draw circle boundary (green)
        cv2.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3) # Draw center (red)
else:
    print("No cells detected!")

#Visualization part of Hough method
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(blurred, cmap='gray')
axes[1].set_title('Gaussian Blur (9x9)')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
axes[2].set_title(f'Detected Cells: {hough_count}')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('method1_hough_circle.png', dpi=300, bbox_inches='tight')
plt.show()

# ----METHOD 2: CANNY + CONTOURS----
#Edge detection + Finding contours
blurred2 = cv2.GaussianBlur(gray, (5, 5), 0) #Gaussian Blur
edges = cv2.Canny(blurred2, 25, 100)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output2 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
count2 = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 30 < area < 4500:
        count2 += 1
        cv2.drawContours(output2, [cnt], -1, (0, 255, 0), 2)
#Visualization for Method 2: Canny + Contours
fig,axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(edges, cmap='gray')
axes[1].set_title('Canny Edge Detection')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
axes[2].set_title(f'Detected Cells: {count2}')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('method2_canny_contours.png', dpi=300, bbox_inches='tight')
plt.show()

# ----METHOD 3: THRESHOLD + BLOBS (CONNECTED COMPOUNDS)----
blurred3 = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blurred3, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
eroded = cv2.erode(binary, kernel, iterations=2)
cleaned = cv2.dilate(eroded, kernel, iterations=1)

num_labels, labels = cv2.connectedComponents(cleaned)
count3 = num_labels - 1

#Visualization
output3 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
contours3, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(output3, contours3, -1, (0, 255, 0), 2)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(cleaned, cmap='gray')
axes[1].set_title('Opened Image')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
axes[2].set_title(f'Detected Cells: {count3}')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('method3_Blobs.png', dpi=300, bbox_inches='tight')
plt.show()

# ----COMPARISON OF ALL METHODS----
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
#Hough
axes[0].imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
axes[0].set_title(f'Method 1: Hough\nCount: {hough_count}')
axes[0].axis('off')
#Canny
axes[1].imshow(cv2.cvtColor(output2, cv2.COLOR_BGR2RGB))
axes[1].set_title(f'Method 2: Canny\nCount: {count2}')
axes[1].axis('off')
#Connected Compounds (blobs)
axes[2].imshow(cv2.cvtColor(output3, cv2.COLOR_BGR2RGB))
axes[2].set_title(f'Method 3: Connected Compounds\nCount: {count3}')
axes[2].axis('off')

plt.tight_layout()
plt.savefig('methods_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nFinal Counts:") #Outputs for all methods
print(f"Method 1 (Hough): {hough_count}")
print(f"Method 2 (Canny): {count2}")
print(f"Method 3 (Connected Components): {count3}")