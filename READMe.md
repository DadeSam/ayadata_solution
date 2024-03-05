# Task 1 Approach













# Task 2
1. I looked at the mask names for a pattern (naming convention)
2. I found out the mask name is equal to mask_id with a png extension
eg 1803242321-00000298_00000.png = 1803242321-00000298_00000 + '.png'
3. I used this logic to write the logic to loop over the contents of the annotations csv file
4. I used the class_name field in the annotations file to create folders for the differing class names identified while looping
5. Modules used are shutil, os, and csv
6. Language is python
7. this script approximately 47 minutes to complete.

NOTE: change the csv_file, image_folder and output_folder paths if you want to run this script on your machine
