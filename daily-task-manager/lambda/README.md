### **`lambda/README.md`**


# Lambda Function: DailyTaskExecutor

This folder contains the AWS Lambda function code and dependencies for the **Daily Task Scheduler** project. The function processes tasks stored in the DynamoDB table and updates their statuses based on the execution logic.

---

## Files

### 1. `lambda_function.py`
- **Purpose**: Core Python script for the Lambda function.
- **Description**: 
  - Scans the `ScheduledTasks` DynamoDB table for tasks marked as "Pending".
  - Processes each task and updates its `Status` to "Completed".
  - Logs execution details in CloudWatch Logs.

### 2. `requirements.txt`
- **Purpose**: Lists the Python dependencies required by the Lambda function.
- **Dependencies**:
  - `boto3`: AWS SDK for Python to interact with DynamoDB and other AWS services.

---

## How the Lambda Function Works

1. **Triggered by EventBridge**:
   - The function is triggered daily based on a schedule configured in EventBridge.

2. **Scans DynamoDB**:
   - It retrieves tasks from the `ScheduledTasks` table where `Status` is "Pending".

3. **Processes Each Task**:
   - Executes logic for each task (e.g., prints task details).
   - Updates the task `Status` to "Completed".

4. **Logs to CloudWatch**:
   - Logs execution details, including task IDs and processing timestamps.

---

## Setup Instructions

### 1. Install Dependencies
If running locally for testing, install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 2. Package and Deploy the Lambda Function
1. Zip the function:
    ```bash
    zip function.zip lambda_function.py
    ```
2. Deploy to AWS Lambda:
    ```bash
    aws lambda create-function \
        --function-name DailyTaskExecutor \
        --runtime python3.9 \
        --role <IAM_ROLE_ARN> \
        --handler lambda_function.lambda_handler \
        --zip-file fileb://function.zip
    ```

### 3. Grant Required Permissions
Ensure the Lambda function role has permissions for:
- **DynamoDB**:
  - `dynamodb:Scan`
  - `dynamodb:UpdateItem`
- **CloudWatch Logs**:
  - `logs:CreateLogGroup`
  - `logs:PutLogEvents`

---

## Example Log Output

Below is a sample log entry generated by the Lambda function, stored in CloudWatch Logs:

```plaintext
Processing task: Daily Backup (ID: task1)
Task Daily Backup completed at 2024-12-23 09:00:00
```

---

## Troubleshooting

### Common Issues
1. **Access Denied Errors**:
   - Ensure the Lambda execution role has the correct permissions for DynamoDB and CloudWatch.

2. **Missing Dependencies**:
   - Verify that `boto3` is included in the Lambda runtime (pre-installed in AWS Lambda Python environments).

3. **EventBridge Not Triggering**:
   - Ensure the EventBridge rule is active and correctly configured.
