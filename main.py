import json

def lambda_handler(event, context):
    # Extract information from the event
    input_data = event.get('input_key', 'Default Value')

    # Perform some logic
    output_data = f"Hello, {input_data}!"

    # Print the result to the console
    print(output_data)

    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps(output_data)
    }
