import numpy as np
import matplotlib.pyplot as plt

def removeGrid():
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])
    
def dispImage(img):
    removeGrid()
    if (len(img.shape) != 3):
        plt.imshow(img, 'gray')
    else:
        plt.imshow(img[:,:,::-1])
