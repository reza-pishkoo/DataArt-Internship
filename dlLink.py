import requests
import sys
import getpass
from os.path import basename


# link = input('URL to download : ')
# link = "https://www.pngfind.com/pngs/m/66-661812_upload-file-icon-png-small-file-image-icon.png"
link = "https://file-examples-com.github.io/uploads/2017/10/file_example_PNG_1MB.png"

defaultPath = '/home/' + getpass.getuser() + '/Desktop/'
specificPathSign = input("It will be download in" + defaultPath + ", Do you want to change the directory?(Y/N) ")
if specificPathSign == 'Y' or specificPathSign == 'y' :
    defaultPath = input('write the desired path: ')

response = requests.get(link, stream=True)
file_name = basename(response.url)

with open(defaultPath + file_name, "wb") as f:
    print("Downloading %s" % file_name)
    total_length = response.headers.get('content-length')

    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
            sys.stdout.flush()



# import sys
# import requests
# import getpass
# from os.path import basename

# # url = 'https://file-examples-com.github.io/uploads/2017/10/file_example_PNG_1MB.png'
# url = input("URL pls: ")

# downloadPath = '/home/' + getpass.getuser() + '/Downloads/'
# specificPath = input("The default path is in " + downloadPath + " directory, Do you want to change it?(Y/N) ")

# if specificPath == "Y":
#     downloadPath = input("Enter the path u want to download in: ")

# response = requests.get(url, stream = True)
# fileName = basename(response.url)

# with open(downloadPath + fileName, 'wb') as f:
#     total_length = response.headers.get('content-length')

#     if total_length is None:
#         f.write(response.content)
#     else:
#         dl = 0
#         total_length = int(total_length)
#         for data in response.iter_content(chunk_size = 4096):
#             dl += len(data)
#             f.write(data)
#             done = int(50 * dl / total_length)
#             sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)) )    
#             sys.stdout.flush()

