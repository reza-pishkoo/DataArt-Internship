import requests
import typer
import sys
import getpass
from os.path import basename

app = typer.Typer()

def download(url: str, filePath: str):
    response = requests.get(url, stream=True)
    fileName = basename(response.url)

    with open(filePath + fileName, 'wb') as f:
        total = response.headers.get('content-length')
        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50 - done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


@app.command()
def cliDownload(url: str): 
    defaultPath = '/home/' + getpass.getuser() + '/Desktop/'
    specificPathSign = input("It will be download in" + defaultPath + ", Do you want to change the directory?(Y/N) ")

    if(specificPathSign == "Y"):
        defaultPath = input('write the desired path: ')
        download(url, defaultPath)
    elif(specificPathSign == "N"):    
        download(url, defaultPath)
    else:
        print("wrong command!")
        cliDownload(url)

if __name__ == "__main__":
    app()

    

