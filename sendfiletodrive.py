# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# google_auth=GoogleAuth()
# drive_app=GoogleDrive()
# upload_list=["log.txt"]

# for file_to_upload in upload_list:
#     file = drive_app.CreateFile({'parent':[{'id':'1uRIFhJJUYB1W-0leI_---Qqu4zYPOk31'}]})
#     file.SetContentFile(file_to_upload)
#     file.Upload()
# import requests

# def get_session_token(email, password, app_id, api_key):
#     url = "https://www.mediafire.com/api/1.5/user/get_session_token.php"
#     payload = {
#         "email": email,
#         "password": password,
#         "application_id": app_id,
#         "signature": api_key
#     }
#     response = requests.get(url, params=payload)
#     result = response.json()
#     return result['response']['session_token']

# def upload_file(file_path, session_token):
#     url = "https://www.mediafire.com/api/1.5/upload/simple.php"
#     files = {'file': open(file_path, 'rb')}
#     payload = {'session_token': session_token}
#     response = requests.post(url, files=files, data=payload)
#     return response.json()

# # Replace these with your actual MediaFire account details and file path
# email = "your_email@example.com"
# password = "your_password"
# app_id = "your_app_id"
# api_key = "your_api_key"
# file_path = "path_to_your_file"

# session_token = get_session_token(email, password, app_id, api_key)
# upload_response = upload_file(file_path, session_token)

# print(upload_response)
from github import Github
# from key import access_token
token=""
accout=Github(token)

# try:
#     organization = accout.get_organization("danh1010")
#     print(f"Organization name: {organization.name}")
# except github.GithubException as e:
#     print(f"Error: {e.data['message']}")

user= accout.get_user("danh1010")
# organ=accout.get_organization("danh1010")
file=r"D:\Isoft\log.txt"

with open(file,'r') as file_content:
    data=file_content.read()

repo=user.get_repo("test")

repo.create_file(
    path='log.txt',
    message="upload file test",
    content=data
)    

print("upload thanh cong")
# for repo in user.get_repos():
#     print(repo.full_name)
