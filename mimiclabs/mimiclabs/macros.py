import os

import mimiclabs


MIMICLABS_TMP_FOLDER = os.path.expanduser(
    os.environ.get(
        "MIMICLABS_TMP_FOLDER", os.path.join(mimiclabs.__path__[0], "mimiclabs", "tmp")
    )
)

SPACEMOUSE_PRODUCT_ID = 50734
# SPACEMOUSE_PRODUCT_ID = 50741 ## uncomment for older model
