import pandas as pd
import numpy as np
from PIL import Image
import os


def preprocess_images(X: pd.DataFrame)-> np.ndarray:

    for image_name in X['Image_name']:
        image_path = os.path.join("../raw_data/Images/", image_name)
        image = Image.open(image_path)
        image = image.resize((100, 100))
        image_array = np.array(image)

        flattened_pixels = image_array.reshape(-1, 3)

    return flattened_pixels
