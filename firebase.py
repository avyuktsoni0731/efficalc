import firebase_admin
from firebase_admin import credentials, storage

cred = credentials.Certificate("./firebase.json")
firebase_admin.initialize_app(cred)

storage_client = storage.bucket('efficiency-calculator-c2190.appspot.com')

def upload_file_to_storage(file_path, destination_blob_name):
    blob = storage_client.blob(destination_blob_name)
    blob.upload_from_filename(file_path)

def download_file_from_storage(source_blob_name, destination_file_path):
    blob = storage_client.blob(source_blob_name)
    blob.download_to_filename(destination_file_path)
  
if __name__ == '__main__':
    file_path = './Avyukt Soni.jpg'
    destination_blob_name = 'uploads/certificate.jpg'

    upload_file_to_storage(file_path, destination_blob_name)

    # source_blob_name = 'uploads/1st.png'
    # destination_file_path = './1st.png'

    # download_file_from_storage(source_blob_name, destination_file_path)
