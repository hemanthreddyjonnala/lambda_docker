# Dockerfile
FROM public.ecr.aws/lambda/python:3.8

# Copy the Lambda handler script
COPY main.py /var/task/

# Set the handler function
CMD ["main.lambda_handler"]