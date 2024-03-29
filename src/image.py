from pathlib import Path
from PIL import UnidentifiedImageError, Image
import os

path = Path("PetImages/Dog").rglob("*.jpg")
for img_p in path:
    try:
        img = Image.open(img_p)
    except UnidentifiedImageError:
            os.remove(img_p)

path = Path("PetImages/Cat").rglob("*.jpg")
for img_p in path:
    try:
        img = Image.open(img_p)
    except UnidentifiedImageError:
            os.remove(img_p)
