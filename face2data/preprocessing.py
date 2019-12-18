from io import BytesIO
from PIL import Image
import numpy as np

IM_WIDTH = IM_HEIGHT = 224


def pre_process_image(img_bytes: bytes) -> np.ndarray:
    """
    Used to perform some minor pre processing on the image before inputting into the network.
    """
    im = Image.open(BytesIO(img_bytes))

    if im.mode != 'RGB':
        im = im.convert('RGB')

    im = im.resize((IM_WIDTH, IM_HEIGHT))
    im = np.array(im) / 255.0
    im = np.expand_dims(im, axis=0)

    return im
