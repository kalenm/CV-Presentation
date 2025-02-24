# A simple demo of k-means clustering used in photo editing

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creates list of images to process along with an output list to draw them later
pics = [cv2.imread('pictures/zune.jpg'),cv2.imread('pictures/gun.jpg'), 
        cv2.imread('pictures/pip.jpg'), cv2.imread('pictures/clouds.jpeg')]
output = []

plt.rcParams["figure.figsize"] = (14,14)
final = plt.figure()


# Bulk of the image processing happens in here
for image in pics:

    # Change image to rgb format for better processing
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Converts the image into a 1x2 and converts 
    pixel_values = image.reshape((-1,3))
    pixel_values = np.float32(pixel_values)

    # This is the fun stuff
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    k = 4
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert the image colors to the calculated centroids and remake the image, then finally add it to the output list
    centers = np.uint8(centers)
    labels = labels.flatten()
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)
    output.append(segmented_image)


#allows for multiple images to be drawn on a single figure - this requires that the code only uses 4 images at a time, not gonna bother fixing it
for i in range(len(output)):
    final.add_subplot(221 + i)
    plt.axis('off')
    plt.imshow(output[i])

plt.savefig(f"pictures/kmeans-{k}.png", bbox_inches='tight')
# plt.show()
