# Import necessary libraries
import boto3
from datetime import datetime

# Initialize the DynamoDB resource
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ScheduledTasks")

def lambda_handler(event, context):
    """
    AWS Lambda handler function that processes tasks from the DynamoDB table
    and updates their status to 'Completed'.
    """
    try:
        # Scan the table for tasks
        tasks = table.scan()["Items"]
        
        for task in tasks:
            task_id = task["TaskID"]
            task_name = task["TaskName"]
            print(f"Processing task: {task_name} (ID: {task_id})")
            
            # Update the task status
            table.update_item(
                Key={"TaskID": task_id},
                UpdateExpression="set #st = :status",
                ExpressionAttributeNames={"#st": "Status"},
                ExpressionAttributeValues={":status": "Completed"}
            )
            
            print(f"Task {task_name} completed at {datetime.now()}")
        
        return {"status": "success"}
    except Exception as e:
        print(f"Error processing tasks: {e}")
        raise

