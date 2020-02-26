// Tested with this version of Terraform
terraform {
  required_version = ">= 0.11.2"
}

# Setup our aws provider
provider "aws" {
  profile     = "default"
  region      = "${var.region}"
}
