#from scipy.misc import imread
from scipy.linalg import norm
#from scipy import sum, average


from PIL import Image
from PIL import ImageChops
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
max=0;
for i in range (1,6000):
    j = i+1
    pic1 = Image.open("C:/temp/motion/dest/Testvideo/"+str('%0.5d' %(i))+".jpg")
    picBW1 = pic1.convert('L')
    picBW1 = picBW1.crop((400,400, 500,500))
    pic2 = Image.open("C:/temp/motion/dest/Testvideo/"+str('%0.5d' %(j))+".jpg")
    picBW2 = pic2.convert('L')
    picBW2 = picBW2.crop((400,400, 500,500))
    diff1 = ImageChops.difference(picBW1,picBW2)
    h = diff1.histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = np.sqrt(sum_of_squares / float(picBW1.size[0] * picBW1.size[1]))
    if rms > max:
        max=rms
        print (rms)


#plt.imshow(diff1)
#plt.show()
