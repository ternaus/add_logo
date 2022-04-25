from typing import Optional

import cv2
import numpy as np


def image_resize(
    image: np.ndarray, width: Optional[int] = None, height: Optional[int] = None, inter: int = cv2.INTER_AREA
) -> np.ndarray:
    # initialize the dimensions of the image to be resized and
    # grab the image size
    (image_height, image_width) = image.shape[:2]

    # if both the width and height are None, then return the original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(image_height)
        dim = (int(image_width * r), height)

    elif height is None:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(image_width)
        dim = (width, int(image_height * r))

    # resize the image
    return cv2.resize(image, dim, interpolation=inter)


def add_logo(image: np.ndarray, logo: np.ndarray, factor: float) -> np.ndarray:
    image_height, image_width = image.shape[:2]

    new_height = int(factor * image_height)

    new_logo = image_resize(logo, height=new_height)

    if new_logo.shape[2] > image_width:
        new_logo = image_resize(logo, width=image_width)

    logo_height, logo_width = new_logo.shape[:2]

    result = image.copy()
    result[-logo_height:, -logo_width:] = new_logo

    return result
