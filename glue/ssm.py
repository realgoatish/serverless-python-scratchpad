import boto3
import os
# note: name of this package is python-dotenv
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")


ssm_client = boto3.client(
  'ssm',
  aws_access_key_id=AWS_ACCESS_KEY_ID,
  aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def get_parameters_by_path(path_prefix):
  """Retrieve all parameters under a given path prefix."""
  parameters = []
  next_token = None
  while True:
      if next_token:
          response = ssm_client.get_parameters_by_path(Path=path_prefix, Recursive=True, NextToken=next_token)
      else:
          response = ssm_client.get_parameters_by_path(Path=path_prefix, Recursive=True)
      parameters.extend(response['Parameters'])
      next_token = response.get('NextToken')
      if not next_token:
          break
  return parameters

# Get all parameters for prod and dev
prod_params = get_parameters_by_path('/prod/lambda/airtableGlue')
dev_params = get_parameters_by_path('/dev/lambda/airtableGlue')

# Extract the parameter names without the prefix
prod_param_names = {param['Name'].split('/prod/lambda/airtableGlue/')[-1] for param in prod_params}
dev_param_names = {param['Name'].split('/dev/lambda/airtableGlue/')[-1] for param in dev_params}

# Find parameters that are in prod but not in dev
missing_in_dev = prod_param_names - dev_param_names

# Create missing parameters in dev
for param_name in missing_in_dev:
  # Find the corresponding prod parameter
  prod_param = next(param for param in prod_params if param['Name'].endswith(param_name))

  # Create the parameter in dev
  ssm_client.put_parameter(
      Name=f'/dev/lambda/airtableGlue/{param_name}',
      Value=prod_param['Value'],
      Type=prod_param['Type'],
      Overwrite=False  # Set to True if you want to overwrite existing parameters
  )

  print(f"Created parameter /dev/lambda/airtableGlue/{param_name} in SSM.")

    