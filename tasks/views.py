from django.shortcuts import render
from todo_app.settings import BASE_DIR

import boto3
import time


# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")


def upload_file(request):

    # Create an S3 client
    s3 = boto3.client('s3')

    filename = "file.txt"
    path_to_file = '{0}/{1}'.format(BASE_DIR, filename)
    bucket_name = 'last-hearth'

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(path_to_file, bucket_name, "{0}.{1}".format(filename, str(time.time())))
    return render(request, "upload-file.html")


def download_file_from_s_three(request):

    print(request)
    with open('download_file.txt', 'w') as f:
        f.write('hello')
        f.close()
