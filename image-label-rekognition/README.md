# Image Label Detection with AWS Rekognition

## Overview of Project ☁️
This project showcases the use of **Amazon Rekognition** to detect and label objects in images stored in **Amazon S3**. The system can identify multiple objects in an image and provide bounding boxes along with confidence levels. For example, the provided image `download.jpg` identifies objects like "German Shepherd" and "Cat".

---

## Detected Labels Example
When running the script with `download.jpg`, the output is:
```plaintext
Detected labels for download.jpg
Label: Animal, Confidence: 97.94%
Label: Canine, Confidence: 97.94%
Label: Dog, Confidence: 97.94%
Label: Mammal, Confidence: 97.94%
Label: Pet, Confidence: 97.94%
Label: German Shepherd, Confidence: 96.35%
Label: Cat, Confidence: 96.08%

Labels detected: 7
```

---

## Steps to Perform 
1. **Set up an Amazon S3 bucket**:
   - Upload the image (e.g., `download.jpg`) to the bucket.
2. **Install and configure AWS CLI**:
   - Install the AWS CLI on your local machine and set up your credentials.
3. **Run the Python script**:
   - The script fetches the image from the S3 bucket, detects labels using Rekognition, and visualizes the results.

---

## Services Used 
- **Amazon S3**: To store images.
- **Amazon Rekognition**: For image label detection.
- **AWS CLI**: To manage resources and permissions via the command line.

---

## Prerequisites
1. **AWS Account**:
   - Ensure your credentials have the following permissions:
     - `rekognition:DetectLabels`
     - `s3:GetObject`
2. **Python 3.x** installed with the following libraries:
   - `boto3`
   - `matplotlib`
   - `Pillow`

Install the required libraries using:
```bash
pip install boto3 matplotlib pillow
```

3. **Configured AWS CLI**:
   - Set up your AWS CLI credentials using:
     ```bash
     aws configure
     ```

---

## Project Structure
```
Cloud-Projects/
  image-label-rekognition/
    reko-example.py           # Python script to detect labels
    download.jpg              # Input image (uploaded to S3)
    architecture-diagram.png  # Optional diagram for documentation
```

---

## Usage

### Step 1: Modify the Script
Update the following variables in `reko-example.py`:
```python
photo = 'download.jpg'  # Name of the image in S3
bucket = 'label-images-rekognition'  # Your S3 bucket name
```

### Step 2: Run the Script
Run the Python script:
```bash
python3 reko-example.py
```

---

## Output Visualization
- The script uses **Matplotlib** to display the image.
- Detected objects are highlighted with bounding boxes and their labels, including confidence levels.

---

## Troubleshooting
1. **Error: InvalidS3ObjectException**:
   - Ensure the file name and bucket name are correct.
   - Verify the file exists in the S3 bucket.

2. **Access Denied**:
   - Confirm the IAM role or credentials have the required permissions (`rekognition:DetectLabels`, `s3:GetObject`).

3. **Image Not Found**:
   - Ensure the image is uploaded to the correct S3 bucket and region.

---

## Future Enhancements
- Add support for processing multiple images in batch mode.
- Save annotated images with bounding boxes back to S3.
- Integrate other AWS Rekognition features like face detection and text recognition.

---

