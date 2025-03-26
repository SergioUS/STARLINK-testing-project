# browserstack.py
import os
import requests

# Import your credentials from my_keys.py (or use environment variables)
from my_keys import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY


def get_session_details(session_id):
    """
    Retrieve session details from BrowserStack using the REST API.
    """
    url = f"https://api.browserstack.com/automate/sessions/{session_id}.json"
    response = requests.get(url, auth=(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get session details. Status code: {response.status_code}")
        return None


def download_artifact(session_id, artifact_type="video", save_dir="./BrowserStackReports"):
    """
    Downloads a BrowserStack artifact (e.g., video) for the given session.

    Parameters:
        session_id (str): The BrowserStack session ID.
        artifact_type (str): The type of artifact to download. Currently only 'video' is handled.
        save_dir (str): The directory where the artifact will be saved.

    Returns:
        file_path (str): The path of the downloaded file, or None if download fails.
    """
    details = get_session_details(session_id)
    if details is None:
        return None

    # Extract the artifact URL based on artifact type.
    if artifact_type.lower() == "video":
        artifact_url = details.get("automation_session", {}).get("video_url")
        file_extension = "mp4"
    else:
        print(f"Artifact type {artifact_type} not supported yet.")
        return None

    if artifact_url:
        response = requests.get(artifact_url, auth=(BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY))
        if response.status_code == 200:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            file_path = os.path.join(save_dir, f"{session_id}_{artifact_type}.{file_extension}")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {artifact_type} artifact to {file_path}")
            return file_path
        else:
            print(f"Failed to download artifact. Status code: {response.status_code}")
    else:
        print("Artifact URL not found in session details.")
    return None


if __name__ == "__main__":
    # For testing purposes, replace 'YOUR_SESSION_ID_HERE' with a real session ID.
    session_id = "YOUR_SESSION_ID_HERE"
    download_artifact(session_id, "video")
