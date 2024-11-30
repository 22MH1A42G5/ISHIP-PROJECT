# ISHIP-PROJECT
## Cross-VPC EC2 Communication in Same Region
### 1. Creating Two VPCs:
###  <ul><li>	Set up two separate Virtual Private Clouds (VPCs) to isolate resources.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/1.jpg" width="700" height="400">
</p>

### 2. Creating Subnets:
### <ul><li> Create one public subnet and one private subnet within each VPC.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/3.jpg" width="700" height="400">
</p>

### 3. Creating Route Tables:
### <ul> <li>Configure two route tables in each VPC, one for the public subnet and one for the private subnet.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/4.jpg" width="700" height="400">
</p>

### 4. Creating Internet Gateways:
### <ul style="list-style-type: square"> <li>	Attach an Internet Gateway to each VPC and associate it with the public subnet to enable internet connectivity.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/5.jpg" width="700" height="400">
</p>

### 5. Creating Peering Connection:
### <ul><li>	Establish a VPC peering connection between the two VPCs to enable communication.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/6.jpg" width="700" height="400">
</p>

### 6. Resource Map:
###	<ul><li>Map the associations between the public and private subnets, route tables, and Internet Gateway connections in First VPC. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/7.jpg" width="700" height="400">
</p>

###	<ul><li>Map the associations between the public and private subnets, route tables, and Internet Gateway connections in Second VPC. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/8.jpg" width="700" height="400">
</p>

### 7. Creating Public EC2 Instances via Cloud9:
### <ul><li>Launch public EC2 instances in each VPC using the AWS Cloud9 service for development purposes.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/9.jpg" width="700" height="400">
</p>

### 8. Accessing Public and Creating Private EC2 Instances:
### <ul><li> Access the public EC2 instances launched from Cloud9. Then, create private EC2 instances within the EC2 service in each VPC. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/10.jpg" width="700" height="400">
</p>

### 9. Connecting Private EC2 Instances:
### <ul><li>Use the public EC2 instances as bastions to connect to the private EC2 instances, and access them through the Cloud9 service.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/ISHIP-PROJECT/blob/main/visuals/11.jpg" width="700" height="400">
</p>
