## Create Glue Job

resource "aws_glue_job" "csv-to-parquet-jobsity-finall" {
  name     = "csv-to-parquet-jobsity-finall"
  role_arn = data.aws_iam_role.AWSGlueServiceRole-trips-chalenge-2.arn
  glue_version = "2.0"
  worker_type = "G.1X"
  number_of_workers = "10"
  command {
    script_location = "s3://spark-glue-job/spark.py"
    python_version = "3"
  }
}