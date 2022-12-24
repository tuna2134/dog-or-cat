import PIL
from pathlib import Path
from PIL import UnidentifiedImageError
import os

path = Path("PetImages/Dog").rglob("*.jpg")
for img_p in path:
    try:
        img = PIL.Image.open(img_p)
    except PIL.UnidentifiedImageError:
            os.remove(img_p)
