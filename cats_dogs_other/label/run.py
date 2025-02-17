import os
from extraction import extract_images

if __name__ == "__main__":
    # Préparation du dataset
    raw_folder = "cats_dogs_other/label/dataset/_raw"
    postprocess_folder = "cats_dogs_other/label/dataset/extract"
    if not os.path.isdir(postprocess_folder) or not os.listdir(postprocess_folder):
        res = extract_images(raw_folder, postprocess_folder)
        print("files input = " + str(res.number_files_input))
        print("files output = " + str(res.number_images_output))