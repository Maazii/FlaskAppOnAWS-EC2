// Here are our security groups. You can see I have allowed ports 5000 and 22.

resource "aws_security_group" "ingress-all-test" {
name = "allow-all-sg"
vpc_id = "${aws_vpc.test-env.id}"
ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 22
    to_port = 22
    protocol = "tcp"
  }

// Port 5000 is also allowed given Flask runs on 5000
ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 5000
    to_port = 5000
    protocol = "tcp"
  }

// Terraform removes the default rule
  egress {
   from_port = 0
   to_port = 0
   protocol = "-1"
   cidr_blocks = ["0.0.0.0/0"]
 }
}