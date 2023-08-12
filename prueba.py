import boto3

def list_buckets():
	s3 = boto3.client('s3')
	buckets_names = [bucket['Name'] for bucket in response['Buckets']]
	return bucket_names

def list_files(bucket_name):
	s3 = boto3.client('s3')
	response = s3.list_objects_v2(Bucket=bucket_name)
	if 'Contents' in response:
		fie_names = [file['Key'] for file in response['Contents']]
		return file_names
	else:
		return []

def upload_file(bucket_name, local_file_path, s3_file_name):
	S3 = boto3.client('s3')
	s3.upload_file(local_file_path, bucket_name, s3_file_name)

def download_file(bucket_name, s3_file_name, local_file_path):
	s3 = boto3.client('s3')
	s3.download_file(bucket_name, s3_file_name, local_file_path)

if __name__ == "__main__":
	buckets = list_buckets()
	print("Bucket names:")
	for bucket in buckets:
		print(bucket)

	target_bucket = 'alejo1'
	files = list_files(target_bucket)
	print(f"Files in '{target_bucket}':")
	for file in files:
		print(file)

	target_bucket = 'alejo1'
	local_file_path = 'prueba2.txt'
	s3_file_name = 'prueba2.txt'
	upload_file(target_bucket, local_file_path, s3_file_name)
	print(f" '{s3_file_name}' uploaded to '{target_bucket}'.")

	local_file_path = ''
	download_file(target_bucket, s3_file_name, f'desc_{local_file_path}')
	print(f"'{s3_file_name}' downloaded from '{target_bucket}' to '{local_file_path}'.")