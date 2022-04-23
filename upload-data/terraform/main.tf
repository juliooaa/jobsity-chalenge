provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

data "aws_iam_role" "AWSGlueServiceRole-trips-chalenge-2" {
  name = "AWSGlueServiceRole-trips-chalenge-2"
}