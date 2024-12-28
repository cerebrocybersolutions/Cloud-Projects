import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

def detect_labels(photo, bucket):
    client = boto3.client('rekognition')
    
    try:
        # Detect labels
        response = client.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
            MaxLabels=10)
    except Exception as e:
        print(f"Error calling Rekognition: {e}")
        return 0

    print('Detected labels for ' + photo)
    for label in response['Labels']:
        print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%\n")
    
    # Load image from S3
    s3 = boto3.resource('s3')
    try:
        obj = s3.Object(bucket, photo)
        img_data = obj.get()['Body'].read()
        img = Image.open(BytesIO(img_data))
    except Exception as e:
        print(f"Error loading image from S3: {e}")
        return 0

    # Display the image and bounding boxes
    visualize_labels(img, response['Labels'])
    return len(response['Labels'])

def visualize_labels(img, labels):
    plt.imshow(img)
    ax = plt.gca()

    for label in labels:
        for instance in label.get('Instances', []):
            bbox = instance['BoundingBox']
            left = bbox['Left'] * img.width
            top = bbox['Top'] * img.height
            width = bbox['Width'] * img.width
            height = bbox['Height'] * img.height

            rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            label_text = f"{label['Name']} ({label['Confidence']:.2f}%)"
            plt.text(left, top - 2, label_text, color='r', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

    plt.show()

def main():
    photo = 'download.jpg'
    bucket = 'label-images-rekognition'
    label_count = detect_labels(photo, bucket)
    print("Labels detected:", label_count)

if __name__ == "__main__":
    main()

