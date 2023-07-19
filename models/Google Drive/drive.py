from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  

upload_file_list = ['final.txt']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1LgLv3aOWpRDFaIY7naVX2djmEeRwkFrg'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.


