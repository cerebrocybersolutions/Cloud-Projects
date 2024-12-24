# EventBridge Rule: DailyTaskSchedulerRule

This folder contains the configuration and details for the **EventBridge Rule** that triggers the **DailyTaskExecutor Lambda function**.

---

## Rule Details

### Rule Name
`DailyTaskSchedulerRule`

### Schedule
The rule is scheduled to run daily at 9:00 AM UTC:
```bash
cron(0 9 * * ? *)

