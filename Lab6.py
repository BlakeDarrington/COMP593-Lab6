import requests
import hashlib
import subprocess
import os

def main():

    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/'

    sha_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()
    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):
        print("Hash values match")
    
        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)
        print("Ran installer")

        # Delete the VLC installer from disk
        delete_installer(installer_path)
        print("Deleted the installer")

def get_expected_sha256(file):
    resp_msg = requests.get(file)
    return 

def download_installer(file_url):


    return

def installer_ok(installer_data, expected_sha256):
    hash = hashlib.sha256(installer_data).hexdigest()
    if hash == expected_sha256:
        print("The integrity of the installer file has been verified.")
    else:
        print("The hash value of the download installer does not match the expected hash value. The installer file may be infected with malware.")

    return True

def save_installer(installer_data):
    temp_folder = os.getenv('TEMP')
    installer_path = os.path.join(temp_folder, "vlc-3.0.17.4-win64.exe")
    with open(installer_path, "wb") as file:
        file.write(file)
    return

def run_installer(installer_path):
    subprocess.run([installer_path, '/L=1033', '/S'])
    return 
    
def delete_installer(installer_path):
    os.remove(installer_path)
    return


if __name__ == '__main__':
    main()