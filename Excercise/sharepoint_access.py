from google.cloud import storage
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

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
BgProject="polynomial-park-317018"
StorageName="sharepoint-nssl-data"
client = storage.Client.from_service_account_json(json_credentials_path='share_point.json')
bucket = client.get_bucket('sharepoint-nssl-data')

def fun_downloadfile(file_name, folder_name):
     conn = fun_SharePointauth()
     print("connection",conn)
     #Variable to store SharePoint file URL
     #file_url = f'/sites/{SHAREPOINT_SITE_NAME}/{SHAREPOINT_DOC}/{folder_name}/{file_name}'
     file_url = f'https://nationalshunt.sharepoint.com/:x:/r/sites/CustomerSuccess/_layouts/15/Doc.aspx?action=edit&sourcedoc=%7Bdcbbd994-b9f2-4cf8-81a7-374d4ecd60f1%7D&wdOrigin=TEAMS-ELECTRON.teamsSdk.openFilePreview&wdExp=TEAMS-CONTROL&web=1'
     #print(file_url)
     #To open a file in binary format
     file = File.open_binary(conn, file_url)
     open('ramoji', 'wb').write(file.content)
     print(file.raw)
     #return the file contents
     return file.content

def fun_uploadfile(file_n, file_obj):
    contents = file_obj
    destination_blob_name = file_n
    # display the destination of the file
    print(destination_blob_name)
    blob = bucket.blob(destination_blob_name)
    # upload the file into GCS
    blob.upload_from_string(contents)
    print("File successfully uploaded to GCS.")

def fun_get_file(file_n, folder):
    # get the binary content from the file after downloading
    file_obj = fun_downloadfile(file_n, folder)
    # upload the file into GCS
    fun_uploadfile(file_n, file_obj)

#fun_get_file('lakshmoji.txt','')

#authenticate_implicit_with_adc('sandbox-data-etl')

fun_uploadfile('lakshmoji.txt',"kumar")