from google.cloud import storage
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
#from google.cloud import bigquery

#local variables to store the credentials
#the credentials may be store any json or other file
#from pandas.tests.io.test_gbq import bigquery
#from pandas.tests.io.test_gbq import bigquery

USERNAME = "pmishra@nationalshunt.com"
PASSWORD = "kfjndvznwttgtfyd"
SHAREPOINT_SITE = "https://nationalshunt.sharepoint.com"
SHAREPOINT_SITE_NAME = "/Documents/General"
SHAREPOINT_DOC = "VenTestingSheet.xlsx"
#Authentication function
def fun_SharePointauth():
    #local variable to return the connection after authentication
    conn = ClientContext(SHAREPOINT_SITE).with_credentials(UserCredential(USERNAME,PASSWORD))
    #return authentication variable
    return conn
#local variables for credentails
service_account_json = "share_point.json"
#service_account_json="ramoji.json"
BgProject="polynomial-park-317018"
StorageName="sharepoint-nssl-data"
# Construct a BigQuery client object.
#bq_client = bigquery.Client()
#storage_client = storage.Client()
client = storage.Client.from_service_account_json(json_credentials_path='share_point.json')
bucket = client.get_bucket('sharepoint-nssl-data')
#bucket = storage_client.get_bucket(StorageName)
#function to download the file from SharePoint
#file_name which is going to be downloaded
#folder_name of the file's location
def fun_downloadfile(file_name, folder_name):
     conn = fun_SharePointauth()
     print("connection",conn)
     #Variable to store SharePoint file URL
     #file_url = f'/sites/{SHAREPOINT_SITE_NAME}/{SHAREPOINT_DOC}/{folder_name}/{file_name}'
     file_url = f'https://nationalshunt.sharepoint.com/:x:/r/sites/CustomerSuccess/_layouts/15/Doc.aspx?action=edit&sourcedoc=%7Bdcbbd994-b9f2-4cf8-81a7-374d4ecd60f1%7D&wdOrigin=TEAMS-ELECTRON.teamsSdk.openFilePreview&wdExp=TEAMS-CONTROL&web=1'
     print(file_url)
     #To open a file in binary format
     file = File.open_binary(conn, file_url)
     open('ramoji', 'wb').write(file.content)
     print(file.raw)
     #return the file contents
     return file.content


# function to upload a file to GCS
# file_n : name of the file
# file_obj: contents inside the file
def fun_uploadfile(file_n, file_obj):
    # The contents to upload to the file
    contents = file_obj
    # The ID of your GCS object
    destination_blob_name = file_n
    # display the destination of the file
    print(destination_blob_name)
    # bucket variable
   # bucket = bq_client.bucket(bucket_name)
    #bucket = client.get_bucket('sharepoint-nssl-data')
    # pass destination bucket name to blob
    blob = bucket.blob(destination_blob_name)
    # upload the file into GCS
    blob.upload_from_string(contents)
    print("File successfully uploaded to GCS.")


# function to get the file from SharePoint
# file_n : file name of the file in SharePoint
# folder : folder/directory name of the file's location
def fun_get_file(file_n, folder):
    # get the binary content from the file after downloading
    file_obj = fun_downloadfile(file_n, folder)

    # upload the file into GCS
    fun_uploadfile(file_n, file_obj)


#fun_get_file('lakshmoji.txt','')

#authenticate_implicit_with_adc('sandbox-data-etl')

fun_uploadfile('lakshmoji.txt',"kumar")