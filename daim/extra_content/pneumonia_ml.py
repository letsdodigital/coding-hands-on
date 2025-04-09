import numpy as np
from matplotlib import pyplot as plt
import os
from PIL import Image, ImageOps
from torchvision.transforms import functional as F
from tensorflow import keras

top_dir = "./chest_xray/"

# PREPROCESSING


def crop_and_scale(img, target_size):

    # Check that target size is square
    if target_size[0] != target_size[1]:
        raise ValueError("Target size must be square.")

    # Crop the center of the image
    # https://stackoverflow.com/questions/16646183/crop-an-image-in-the-centre-using-pil

    height, width = img.size
    square_size = min(height, width)
    img = F.center_crop(img, square_size)

    # Resize the image
    img = F.resize(img, target_size)
    return ImageOps.grayscale(img)


def get_batch(dir_name, total_size, batch_size, target_img_size):

    # Get an equal number of NORMAL and PNEUMONIA images
    normal_path = os.path.join(top_dir + dir_name + "NORMAL/")
    pneumonia_path = os.path.join(top_dir + dir_name + "PNEUMONIA/")

    norm_img_names = [normal_path + name for name in os.listdir(normal_path)]
    pneu_img_names = [
        pneumonia_path + name for name in os.listdir(pneumonia_path)
    ]

    # Add the two sets together and shuffle them
    img_names = norm_img_names + pneu_img_names
    np.random.shuffle(img_names)

    # Pick a sample from the shuffled data
    target_imgs = img_names[0:total_size]

    # Split the images into batches.
    img_batches = [
        target_imgs[i : i + batch_size]
        for i in range(0, len(target_imgs), batch_size)
    ]

    # Load each target image

    for batch in img_batches:
        batch_dat = np.zeros([batch_size] + list(target_img_size))
        labels = np.zeros([batch_size])

        for i, img_name in enumerate(batch):
            img = Image.open(img_name)
            img = crop_and_scale(img, target_img_size)
            batch_dat[i] = np.array(img) / 255.0

            # Set the label for the image
            labels[i] = 1.0 if "PNEUMONIA" in img_name else 0.0

        yield batch_dat, labels


img_size = (64, 64)
input_size = list(img_size) + [1]  # Change to expand dims

# Create the model
model = keras.Sequential(
    [
        keras.Input(shape=input_size),
        keras.layers.Conv2D(32, 5, activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Conv2D(128, 3, activation="relu"),
        keras.layers.MaxPooling2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(32, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ]
)
model.summary()

# Compile the model with an appropriate loss function
model.compile(
    loss=keras.losses.BinaryCrossentropy(),
    optimizer="adam",
    metrics=["accuracy", keras.metrics.Precision(), keras.metrics.Recall()],
)

# Train model on dataset
# https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly

train_gen = get_batch("train/", 1024 * 10, 8, img_size)
val_gen = get_batch("val/", 4 * 10, 1, img_size)

model.fit(
    train_gen,
    epochs=10,
    steps_per_epoch=1024 / 8,
    validation_data=val_gen,
    validation_batch_size=1,
    validation_steps=32 / 8,
)
