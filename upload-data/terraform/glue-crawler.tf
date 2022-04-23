## Create crawler

resource "aws_glue_crawler" "trips-crawler" {
    database_name = aws_glue_catalog_database.glue-database-jobsity.id
    name = "trips-crawler"
    role = data.aws_iam_role.AWSGlueServiceRole-trips-chalenge-2.arn
    s3_target {
      path = "s3://${aws_s3_bucket.chalenge-trips-jobsity.bucket}"
    }
}