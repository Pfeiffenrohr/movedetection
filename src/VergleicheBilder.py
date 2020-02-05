#from scipy.misc import imread
from scipy.linalg import norm
#from scipy import sum, average

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None

from PIL import Image
from PIL import ImageChops
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
pic1 = Image.open("../bilder/00004.jpg")
picBW1 = pic1.convert('L')
picBW1 = picBW1.crop((400,400, 500,500))
pic2 = Image.open("../bilder/00005.jpg")
picBW2 = pic2.convert('L')
picBW2 = picBW2.crop((400,400, 500,500))
diff=equal(picBW1,picBW2)
print (diff)
diff1 = ImageChops.difference(picBW1,picBW2)
h = diff1.histogram()
sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
sum_of_squares = sum(sq)
rms = np.sqrt(sum_of_squares / float(picBW1.size[0] * picBW1.size[1]))
print (rms)

#plt.imshow(diff1)
#plt.show()
