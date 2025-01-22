import os
import platform
import shutil
import requests


def download_file(url: str, file_name: str) -> None:
    """
    Downloads a file from the specified URL. If the system is Linux and 'wget' is available,
    it uses 'wget' for the download. Otherwise, it falls back to using the requests library.

    Args:
        url (str): The URL of the file to download.
        file_name (str): The name to save the downloaded file as.

    Raises:
        Exception: If the download fails using both methods.
    """
    # Check if the system is Linux and if 'wget' is available
    is_linux = platform.system() == "Linux"
    has_wget = shutil.which("wget") is not None

    if is_linux and has_wget:
        # Use wget if conditions are met
        print("Using wget...")
        os.system(f"wget -O {file_name} {url}")
    else:
        # Fallback to requests
        print("Using requests...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"File saved as {file_name}")
        else:
            raise Exception(f"Failed to download file. Status code: {response.status_code}")
