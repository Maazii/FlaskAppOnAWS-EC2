variable "ami_id" {
    description = "Image ID for the instance."
    type = string
    default = "ami-005fc0f236362e99f"
}
variable "ami_name" {
    description = "Tag for the Instance; Can be user-defined."
    type = string
    default = "TheCommoner"
}
variable "ami_key_pair_name" {
    description = "The name of the Network Keypair"
    type = string
    default = "WebApplicationPair"
}