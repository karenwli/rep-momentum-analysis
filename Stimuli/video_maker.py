from PIL import Image
import os
import cv2
import ffmpeg

def resize_images(mydir):
    for file in os.listdir(mydir):
        if file.endswith(".jpg"):
            img = file
            Image.resize("300")

    return file

def make_gifs(mydir):

    dir_array = []
    
    return mydir

def make_vids(mydir):
    return mydir

target_dir = "C:\\Users\\nancy\\Desktop\\stimuli\\stimuli\\Target"
filler_dir = "C:\\Users\\nancy\\Desktop\\stimuli\\stimuli\\Filler"

cutoff_array = [25, 50, 75]
# Set the frame rate of the output -- lower is slower
frame_rate = 5

dir_array = [x[0] for x in os.walk(target_dir)] + [x[0] for x in os.walk(filler_dir)]

for img_dir in dir_array:
    tag = img_dir.split("\\")[-1]
    if tag == "Target" or tag == "Filler":
        continue

    for cutoff in cutoff_array:
        # Name each file and make into mp4
        output_file = "C:\\Users\\nancy\\Desktop\\" + tag + str(cutoff) + ".mp4"

        # Get the list of image files
        img_files = sorted([os.path.join(img_dir, f) for f in os.listdir(img_dir) if f.endswith('.jpg')])
        quantity = len(img_files)

        # Decide which subset of images to use based on cutoff point
        if quantity == 21:
            final_index = int(cutoff/5 + 1)
            img_files = img_files[0:final_index]
        elif quantity == 34:
            final_index = int(round(cutoff/3) + 1)
            img_files = img_files[0:final_index]
        else:
            print("Directory '"+ tag + "' has " + str(quantity) + " files")
            continue

        # Get the first image to determine the size of the output video
        img = cv2.imread(img_files[0])
        height, width, channels = img.shape

        # Create a video writer object
        out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

        # Loop through the image files and add them to the video writer object
        for img_file in img_files:
            img = cv2.imread(img_file)
            out.write(img)

        # Release the video writer object
        out.release()

        # Convert the video to mp4 using FFmpeg
        ffmpeg.input(output_file).output(output_file).run()



# Change all images to 300 pixel width
# Create mp4s for each event at 3 stages