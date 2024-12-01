import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentDB')

def lambda_handler(event, context):
    method = event['httpMethod']
    path = event['path']
    body = json.loads(event.get('body', '{}')) if event.get('body') else {}

    if method == "GET" and path == "/students":
        # Get all students
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Items', []))
        }

    elif method == "GET" and path.startswith("/students/"):
        # Get student by RollNo
        roll_no = path.split('/')[-1]
        response = table.get_item(Key={'RollNo': roll_no})
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Student not found'})
        }

    elif method == "POST" and path == "/students":
        # Add a new student
        if not body or not body.get('RollNo'):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'RollNo is required'})
            }
        
        try:
            # Dynamically add the entire body to DynamoDB
            table.put_item(Item=body)
            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'Student added successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error adding student', 'error': str(e)})
            }

    elif method == "PUT" and path.startswith("/students/"):
        # Update a student record
        roll_no = path.split('/')[-1]  # Extract RollNo from the URL path

        if not body or not roll_no:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'RollNo and request body are required'})
            }

        try:
            # Construct the UpdateExpression dynamically based on fields in the body
            update_expression = "SET " + ", ".join([f"#{key} = :{key}" for key in body.keys()])
            
            # Map field names to placeholders to avoid reserved keyword conflicts
            expression_attribute_names = {f"#{key}": key for key in body.keys()}
            
            # Map field values to placeholders for DynamoDB
            expression_attribute_values = {f":{key}": value for key, value in body.items()}

            # Perform the update in DynamoDB
            table.update_item(
                Key={'RollNo': roll_no},  # Specify the primary key (partition key)
                UpdateExpression=update_expression,  # Dynamically constructed update expression
                ExpressionAttributeNames=expression_attribute_names,  # Map field names
                ExpressionAttributeValues=expression_attribute_values  # Map field values
            )

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Student updated successfully'})
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error updating student', 'error': str(e)})
            }


    elif method == "DELETE" and path.startswith("/students/"):
        # Delete a student record
        roll_no = path.split('/')[-1]

        # Attempt to delete the item from DynamoDB
        response = table.delete_item(
            Key={'RollNo': roll_no},
            ReturnValues="ALL_OLD"  # This will return the old item if it exists
        )

        # Check if the item was found and deleted
        if 'Attributes' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': f'Student with RollNo {roll_no} not found'})
            }

        # If the item was deleted
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Student deleted successfully'})
        }

    return {
        'statusCode': 400,
        'body': json.dumps({'message': 'Invalid request'})
    }
