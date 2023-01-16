from PIL import Image
import os


# -----VARIABLES FOR SETTINGS-----
# Directory with image before processing
# Leave "./" if you take a image from the directory with the script
directory_image_before_processing = "./"

# Directory with image after processing
directory_image_after_processing = "squareImages"

# Multiplier
scale = 1

# The color of the filling space
border_color = "white"

# Extensions of images
FILE_EXTENSIONS = ["png", "jpeg", "jpg"]
# ---------------------------


# -----------LOGIC-----------
# Make directory for square image
if directory_image_after_processing not in os.listdir():
    os.mkdir(directory_image_after_processing)

# We sort out all the images in the directory
for image_path in os.listdir(directory_image_before_processing):
    # Check that this is a image
    if image_path.split(".")[-1] in FILE_EXTENSIONS:
        # Load the old image
        old_img = Image.open(
            f"{directory_image_before_processing}/{image_path}")

        # The dimensions of the old image
        width, height = old_img.size

        if width > height:
            # The thickness of the border
            border = width - height

            # New Image, on top of which the old
            new_image = Image.new(
                old_img.mode,  # Color scheme
                (
                    old_img.size[0],  # Horizontal sizes
                    old_img.size[1] + border  # Vertical sizes
                ),
                border_color)  # Set the color

            # Overlaying the old image for a new indent
            new_image.paste(old_img, (0, border // 2))

        elif height > width:
            # The thickness of the border
            border = height - width

            # New Image, on top of which the old
            new_image = Image.new(
                old_img.mode,  # Color scheme
                (
                    old_img.size[0] + border,  # Horizontal sizes
                    old_img.size[1]  # Vertical sizes
                ),
                border_color)  # Set the color

            # Overlaying the old image for a new indent
            new_image.paste(old_img, (border // 2, 0))

        else:
            # New Image, on top of which the old
            new_image = Image.new(
                old_img.mode,  # Color scheme
                (
                    old_img.size[0],  # Horizontal sizes
                    old_img.size[1]  # Vertical sizes
                ),
                border_color)  # Set the color

        # Scaling
        scale_img = new_image.resize(
            (
                round(width * scale),
                round(width * scale)
            ))

        # Save
        scale_img.save(
            f'{directory_image_after_processing}/{image_path.split(".")[0]}_squared.{image_path.split(".")[1]}')
