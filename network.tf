resource "aws_vpc" "test-env" { // aws_vpc represents our Virtual Private Cloud or Network
  cidr_block = "10.0.0.0/16"  // This is the address range
  enable_dns_hostnames = true
  enable_dns_support = true
  tags = {
    Name = "test-env"
  }
}


// This is our elastic IP, or simply our IP address.

resource "aws_eip" "ip-test-env" { // aws_eip represents the elastic IP
  instance = "${aws_instance.test-ec2-instance.id}"
  domain   = "vpc"
}