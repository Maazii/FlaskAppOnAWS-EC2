// We need a gateway so to route data packets to our machine in the cloud.

resource "aws_internet_gateway" "test-env-gw" {
  vpc_id = "${aws_vpc.test-env.id}"
tags = {
    Name = "test-env-gw"
  }
}