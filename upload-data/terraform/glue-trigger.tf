## Trigger for Glue Job

resource "aws_glue_trigger" "trigger-jobsity" {
  name     = "trigger-jobsity"
  schedule = "cron(15 12 * * ? *)"
  type     = "SCHEDULED"

  actions {
    job_name = aws_glue_job.csv-to-parquet-jobsity-finall.name
  }
}