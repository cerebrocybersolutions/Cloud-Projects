import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

def detect_labels(photo, bucket):
    # Initialize Rekognition client
    client = boto3.client('rekognition')

    try:
        # Detect labels in the image
        response = client.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
            MaxLabels=10
        )
    except Exception as e:
        print(f"Error calling Rekognition: {e}")
        return 0

    print(f'Detected labels for {photo}')
    for label in response['Labels']:
        print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%\n")

    # Load the image from S3
    s3 = boto3.resource('s3')
    try:
        obj = s3.Object(bucket, photo)
        img_data = obj.get()['Body'].read()
        img = Image.open(BytesIO(img_data))
    except Exception as e:
        print(f"Error loading image from S3: {e}")
        return 0

    # Visualize the labels and bounding boxes
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

            rect = patches.Rectangle((left, top), width, height, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            label_text = f"{label['Name']} ({label['Confidence']:.2f}%)"
            plt.text(left, top - 5, label_text, color='r', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

    plt.axis('off')
    plt.show()

def main():
    photo = 'download.jpg'  # Update this with the correct image name
    bucket = 'label-images-rekognition'  # Update this with your bucket name

    label_count = detect_labels(photo, bucket)
    print(f"Labels detected: {label_count}")

if __name__ == "__main__":
    main()

