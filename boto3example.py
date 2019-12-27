import boto3
import uuid

def create_bucket_name(bucket_prefix):
    # the generated bucket name must be between 3 and 63 characters
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': current_region})

    print(bucket_name, current_region)
    return bucket_name, bucket_response

def create_temp_file(size, file_name, file_content):
    randon_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(randon_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return randon_file_name