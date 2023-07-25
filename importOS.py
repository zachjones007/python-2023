import os

# Define paths
root_directory = './files'
pdf_directory = './pdf'
image_directory = './images'

# Create directories if they don't exist
if not os.path.exists(pdf_directory):
    os.mkdir(pdf_directory)

if not os.path.exists(image_directory):
    os.mkdir(image_directory)

# Iterate through each sub-directory in the root directory
for subdir, dirs, files in os.walk(root_directory):
    for file in files:
        # Create full path to the file
        file_path = os.path.join(subdir, file)
        
        # Move PDFs and images to their respective directories using os.rename
        if file.endswith('.pdf'):
            os.rename(file_path, os.path.join(pdf_directory, file))
        elif file.endswith('.jpg'):
            os.rename(file_path, os.path.join(image_directory, file))

# Print directory listings and total number of files
def print_directory_contents(directory):
    print(f"\nContents of {directory}:")
    files = os.listdir(directory)
    for file in files:
        print(file)
    print(f"Total number of files in {directory}: {len(files)}")

print_directory_contents(pdf_directory)
print_directory_contents(image_directory)
