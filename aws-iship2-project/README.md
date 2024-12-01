# ISHIP-PROJECT-2
## StudentVault: A Serverless API for Student Management
### 1. Create DynamoDB Table:
### <ul><li> Created a table in DynamoDB for storing student information. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/1.png" width="700" height="400">
</p>


### 2. Create Lambda Function:
### <ul><li> Created a Lambda function named serverless-api using Python. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/2.png" width="700" height="400">
</p>

### <ul><li> Created a new role named serverless-api-role for the Lambda function. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/3.png" width="700" height="400">
</p>

### 3. Write Lambda Code:
### <ul><li> Implemented Lambda code to handle CRUD operations with DynamoDB.</li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/6.png" width="700" height="400">
</p>

### 4. Set Up API Gateway:
### <ul><li> Created a new REST API named StudentVault-API. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/4.png" width="700" height="400">
</p>

### <ul><li> Added resources and methods for POST, GET, PUT, and DELETE. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/5.png" width="700" height="400">
</p>

### <ul><li> Integrated each API Gateway method with the serverless-api Lambda function. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/7.png" width="700" height="400">
</p>

### 5. Update Lambda Role:
### <ul><li> Updated the serverless-api-role to include the following policies: <ul> <li>AmazonDynamoDBFullAccess (to allow full access to DynamoDB). </li> <li> CloudWatchLogsFullAccess (to allow logging for debugging and monitoring). </li></ul></li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/8.png" width="700" height="400">
</p>

### 6. Test POST Method in API Gateway Console:
### <ul><li> Used the API Gateway test console to verify that the POST method correctly adds items to DynamoDB </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/9.png" width="700" height="400">
</p>

### <ul><li> Checked the DynamoDB table to confirm that the new item was successfully added. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/10.png" width="700" height="400">
</p>

### 7. Deploy API:
### <ul><li> Deployed the API to a new stage named prod. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/11.png" width="700" height="400">
</p>

### 8. Test API with Postman:
### <ul><li> Used Postman to test the API functionality. </li></ul>
### <ul><li> GET method: Retrieve all student records from DynamoDB. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/12.png" width="700" height="400">
</p>

### <ul><li> POST method: Add a new student record to DynamoDB. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/13.png" width="700" height="400">
</p>

### <ul><li> GET method with RollNo in the path: Retrieve a specific student's information using their RollNo. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/14.png" width="700" height="400">
</p>

### <ul><li> PUT method: Update a specific student's information in DynamoDB. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/15.png" width="700" height="400">
</p>

### <ul><li> DELETE method: Remove a student record from DynamoDB. </li></ul>
<p align="center">
  <img src="https://github.com/22MH1A42G5/cloud-projects/blob/main/aws-iship2-project/images/16.png" width="700" height="400">
</p>



