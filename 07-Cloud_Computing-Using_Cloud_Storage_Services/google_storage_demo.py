"""
Google Platform for Storage.
Requirements:
Install Google Cloud SDK from: https://cloud.google.com/sdk/docs/install
Run the script named "install.sh" in superuser mode and be sure that gutils component is installed.
Then, run gcloud init and follow the authentication procedure.
Create a new project with : gcloud projects create <project_name>
"""

from gcloud import storage
import os

PROJECT_NAME = "storage-demo-cc"
BLOB_FILENAME = 'blob_file.txt'
KEY_PATH = "storage-demo-cc-b1363b8cc0eb.json" # path to json service-acount key
BUCKET_NAME = "cc2020_2021_test_bucket" #must be unique
os.environ.setdefault("GCLOUD_PROJECT",PROJECT_NAME)
"""
Authentication with json file.
In Google Cloud Platform navigate to "Service Accounts" and create
a new service account for the project. Then, export the credentials 
in json format and save it. 
MAKE SURE that Google Storage Admin permission is granted!
This is not the unique method to manage keys, more can be found on official documentation. 
Make sure that billing mode is associated to the project. Thus, Check in Google SDK
the project billing section and add the billing to the created project. 
"""
client = storage.Client.from_service_account_json(KEY_PATH)

#create a bucket
#bucket = client.create_bucket(BUCKET_NAME)

#open an existent bucket
bucket = client.bucket(BUCKET_NAME)

blob = bucket.blob(BLOB_FILENAME)
blob.upload_from_string('Welcome to a new bucket')
blob.make_public()
