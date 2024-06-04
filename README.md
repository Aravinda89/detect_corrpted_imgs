# Detect and Remove Corrupted Image Files in an Image Dataset Using Python

## Introduction

When working with large image datasets, corrupted images can cause significant issues during AI model training. Detecting and removing these corrupted files is essential to ensure smooth and uninterrupted training processes. This script uses Python and the `Pillow` library to automate the task of scanning directories, identifying corrupted image files, and removing them.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.6 or higher)
- Pillow library

You can install the Pillow library using pip:

```bash
pip install pillow
```

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/corrupted-image-detector.git
   cd corrupted-image-detector
   ```

2. **Set Up Your Environment**:
   Make sure Python and Pillow are installed. If not, install Pillow with:
   ```bash
   pip install pillow
   ```

3. **Run the Script**:
   Pass the path to your image dataset as an argument when running the script:
   ```bash
   python clean_images.py /path/to/your/dataset
   ```
