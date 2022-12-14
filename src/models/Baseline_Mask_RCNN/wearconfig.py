from maskrcnn.mrcnn.config import Config

class WearConfig(Config):
    """Configuration for training on the tool wear dataset.
    Derives from the base Config class and overrides values specific
    to the tool wear dataset.
    """
    # Give the configuration a recognizable name
    NAME = "tool_wear"

    # Train on 1 GPU and 4 images per GPU. We can put multiple images on each
    # GPU because the images are small. Batch size is 4 (GPUs * images/GPU).
    GPU_COUNT = 1
    IMAGES_PER_GPU = 4

    # Number of classes (including background)
    NUM_CLASSES = 1 + 3  # background + ok/nok/doubt

    # Use small images for faster training. Set the limits of the small side
    # the large side, and that determines the image shape.
    IMAGE_MIN_DIM = 320
    IMAGE_MAX_DIM = 320

    # Use smaller anchors because our image and objects are small
    RPN_ANCHOR_SCALES = (16, 32, 64, 128, 256)  # anchor side in pixels

    # Reduce training ROIs per image because the images are small and have
    # few objects. Aim to allow ROI sampling to pick 33% positive ROIs.
    TRAIN_ROIS_PER_IMAGE = 128

    # use small validation steps since the epoch is small
    VALIDATION_STEPS = 20