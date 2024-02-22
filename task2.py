import csv
import os
import shutil

# Path to the CSV file
csv_file = r'C:\Users\Uni-Protech computer\Downloads\Compressed\Task 2\Task 2\mask-images\instance_mask_annotations.csv'

# Path to the folder containing the images
image_folder = r'C:\Users\Uni-Protech computer\Downloads\Compressed\Task 2\Task 2\mask-images\masks'

# Path of folder to save the grouped images
output_folder = r'C:\Users\Uni-Protech computer\Downloads\Compressed\Task 2\Task 2\mask-images\separated_images'

# Checking output folder if it doesn't exist, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Reading the CSV file and group images in read mode
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skipping the header row
    for row in reader:
        image_id, mask_id, class_name = row
        image_path = os.path.join(image_folder, mask_id + '.png')
        output_class_folder = os.path.join(output_folder, class_name)
        if not os.path.exists(output_class_folder):
            os.makedirs(output_class_folder)
        shutil.copy(image_path, output_class_folder)
        print(f"Moved {mask_id}.png to {class_name} folder.")