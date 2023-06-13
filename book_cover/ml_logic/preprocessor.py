import pandas as pd
import numpy as np
from PIL import Image
import os


def preprocess_images(X: pd.DataFrame, resize_size: tuple)-> np.ndarray:
    """
    INPUT
    X: the DataFrame from which we want to retrieve the image names in the 'Image_name' column

    resize_size: a tuple to which dimensions the images should be resized
    For example (100, 100) resizes the images to 100 x 100 pixels

    OUTPUT
    A numpy array of shape (number of images, pixel length, pixel height, color channels)
    """

    output = []

    for image_name in X['Image_name']:
        image_path = os.path.join("../raw_data/Images/", image_name)
        image = Image.open(image_path)
        image = image.resize(resize_size) # Resizing for speed purposes
        image_array = np.array(image)
        output.append(image_array)

    return np.array(output)
