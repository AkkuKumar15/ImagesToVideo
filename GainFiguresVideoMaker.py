import imageio
import os

# Path to the folder containing all of the pictures that you want to include in the order you want to have them appear
folder_path = r'C:\...'

# List all the image files in the folder (may need to add more if statements if image extensions are different)
images = [img for img in os.listdir(folder_path) if img.endswith(".png")]

# Path to the output video file
output_file = 'C:\...\video.mp4'

# Specify the desired frame rate (frames per second)
output_frame_rate = 10  # Frames per second (1 millisecond per frame)

# Create a list to store the image frames
frames = []

# Loop through each image file and append it to the frames list
for image in images:
    image_path = os.path.join(folder_path, image)
    frame = imageio.imread(image_path)
    frames.append(frame)

# Save the frames as a video using imageio
imageio.mimsave(output_file, frames, fps=output_frame_rate)
