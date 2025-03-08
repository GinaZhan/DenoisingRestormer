import os

dataset_dir = r"D:\Master\Courses\Visual and Mobile Computing Systems\DenoisingProject\DenoisingDNN\models\Restormer\Denoising\Datasets\Downloads\SIDD"
if not os.path.exists(dataset_dir):
    print(f" ERROR: Dataset directory does not exist: {dataset_dir}")
    exit()

noisy_files = []
gt_files = []

# Walk through all subdirectories and collect file names
for root, dirs, files in os.walk(dataset_dir):
    for file in files:
        if "NOISY" in file.upper():
            noisy_files.append(file.replace("NOISY", ""))
        elif "GT" in file.upper():
            gt_files.append(file.replace("GT", ""))

# Convert to sets for comparison
missing_gt = set(noisy_files) - set(gt_files)
missing_noisy = set(gt_files) - set(noisy_files)

# Print results
print(f"Total NOISY images: {len(noisy_files)}")
print(f"Total GT images: {len(gt_files)}")

if missing_gt:
    print(" Missing GT images for:", missing_gt)
if missing_noisy:
    print(" Missing NOISY images for:", missing_noisy)
if not missing_gt and not missing_noisy:
    print(" All images are properly paired!")
