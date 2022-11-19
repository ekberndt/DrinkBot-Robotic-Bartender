import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

this_file = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = this_file + "/imgs"

def read_image(img_name, grayscale=False):
    """ reads an image

    Parameters
    ----------
    img_name : str
        name of image
    grayscale : boolean
        true if image is in grayscale, false o/w
    
    Returns
    -------
    ndarray
        an array representing the image read (w/ extension)
    """

    if not grayscale:
        img = cv2.imread(img_name)
    else:
        img = cv2.imread(img_name, 0)

    return img

def show_image(img_name, title='Fig', grayscale=False):
    """show the  as a matplotlib figure
    
    Parameters
    ----------
    img_name : str
        name of image
    tile : str
        title to give the figure shown
    grayscale : boolean
        true if image is in grayscale, false o/w
    """

    if not grayscale:
        plt.imshow(img_name)
        plt.title(title)
        plt.show()
    else:
        plt.imshow(img_name, cmap='gray')
        plt.title(title)
        plt.show()

# def do_kmeans(data, n_clusters):
#     """Uses opencv to perform k-means clustering on the data given. Clusters it into
#        n_clusters clusters.

#        Args:
#          data: ndarray of shape (n_datapoints, dim)
#          n_clusters: int, number of clusters to divide into.

#        Returns:
#          clusters: integer array of length n_datapoints. clusters[i] is
#          a number in range(n_clusters) specifying which cluster data[i]
#          was assigned to. 
#     """
#     criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
#     _, clusters, centers = kmeans = cv2.kmeans(data.astype(np.float32), n_clusters, bestLabels=None, criteria=criteria, attempts=1, flags=cv2.KMEANS_RANDOM_CENTERS)

#     return clusters

# def cluster_segmentation(img, n_clusters, random_state=0):
#     print((img.shape[1]/2, img.shape[0]/2))
#     img_d = cv2.resize(img, dsize=(int(img.shape[1]/2), int(img.shape[0]/2)), interpolation=cv2.INTER_NEAREST)
    

#     # TODO: Generate a clustered image using K-means
    
#     # first convert our 3-dimensional img_d array to a 2-dimensional array
#     # whose shape will be (height * width, number of channels) hint: use img_d.shape
#     img_w = img_d.shape[1]
#     img_h = img_d.shape[0]
#     img_r = img_d.reshape(img_h * img_w, 3)
    
#     # fit the k-means algorithm on this reshaped array img_r using the
#     # the do_kmeans function defined above.
#     clusters = do_kmeans(img_r, n_clusters)

#     # reshape this clustered image to the original downsampled image (img_d) width and height 
#     cluster_img = clusters.reshape(img_h, img_w)

#     # Upsample the image back to the original image (img) using nearest interpolation
#     img_u = cv2.resize(src=cluster_img, dsize=(img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

#     return img_u.astype(np.uint8)

# def test_cluster(img, n_clusters):
#     # For visualization, we need to scale up the image so it
#     # is in range(256) instead of range(n_clusters).
#     clusters = (cluster_segmentation(img, n_clusters) * (255 / (n_clusters-1))).astype(np.uint8)

#     cv2.imwrite(IMG_DIR + "/cluster.jpg", clusters)
#     clusters = cv2.imread(IMG_DIR + '/cluster.jpg')
#     show_image(clusters, title='cluster')





# test_cluster(test_img_color, 5)

def color_mask(img, lowerR, lowerG, lowerB, upperR, upperG, upperB):
    # Convert from BGR (RGB) colorspace to HSV (Hue / Saturation / Value)
    BGR_to_hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([lowerR, lowerG, lowerB])
    upper_bound = np.array([upperR, upperG, upperB])
    mask = cv2.inRange(BGR_to_hsvFrame, lower_bound, upper_bound)

    # Kernal
    kernal = np.ones((5, 5), "uint8")

    dilated_mask = cv2.dilate(mask, kernal)
    res = cv2.bitwise_and(img, img, mask = mask)

    return res

def test_color_mask(img, lowerR, lowerG, lowerB, upperR, upperG, upperB):
    # For visualization, we need to scale up the image so it
    # is in range(256) instead of range(n_clusters).
    masked_img = color_mask(img, lowerR, lowerG, lowerB, upperR, upperG, upperB)

    cv2.imwrite(IMG_DIR + "/color_mask_img.jpg", clusters)
    clusters = cv2.imread(IMG_DIR + '/color_maks_img.jpg')
    show_image(clusters, title='color_mask_img')

test_img_color = read_image(IMG_DIR + '/legos.jpg')
test_color_mask(test_img_color, 100, 100, 100, 200, 200, 200)