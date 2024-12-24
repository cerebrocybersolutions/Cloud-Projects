# DynamoDB Table: ScheduledTasks

This folder contains the schema and related details for the **DynamoDB** table used in the Daily Task Scheduler project.

---

## Table Details

### Table Name
`ScheduledTasks`

### Attributes

| Attribute Name | Type   | Description                                 |
|----------------|--------|---------------------------------------------|
| `TaskID`       | String | Unique identifier for each task (Primary Key). |
| `TaskName`     | String | Name or description of the task.            |
| `Status`       | String | Current status of the task (`Pending` or `Completed`). |
| `ExecutionTime`| String | Scheduled time for the task execution.      |

### Table Schema

The table uses the following schema:
- **Primary Key**: `TaskID` (Partition Key)
- **Billing Mode**: Pay-per-request (on-demand)

---

## How to Create the Table

You can create the table in DynamoDB using the AWS CLI with the following command:

```bash
aws dynamodb create-table \
    --table-name ScheduledTasks \
    --attribute-definitions AttributeName=TaskID,AttributeType=S \
    --key-schema AttributeName=TaskID,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
