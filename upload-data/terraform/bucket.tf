## Create s3 bucket

resource "aws_s3_bucket" "chalenge-trips-jobsity" {
  bucket = "chalenge-trips-jobsity"

  tags = {
    Name        = "Origin"
    Environment = "Prod"
  }
}