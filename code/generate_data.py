"""
This script generates all raw data files required for the notebooks
"""
import os
import subprocess
import copernicusmarine
from CrocoDash.raw_data_access.datasets import gebco as gb
from pathlib import Path
# Set the working directory to the location of this script
data_dir = Path(__file__).parent.parent / "data"

def main():

    setup_glorys_credentials()
    get_gebco_data()
    checkout_cesm()

def setup_glorys_credentials():
    """
    Set up the credentials for accessing the GLORYS data.
    """
    glorys_username = os.getenv("GLORYS_USERNAME")
    glorys_password = os.getenv("GLORYS_PASSWORD")

    copernicusmarine.login(
    username = glorys_username,
    password = glorys_password)


def get_gebco_data():
    """
    Download and process the GEBCO data file.
    """

    if not (data_dir/"GEBCO_2024.nc").exists():
        gb.get_gebco_data_script(output_dir=data_dir, output_file="GEBCO_2024.nc")
        subprocess.run(["chmod", "-R", "755", str(data_dir / "get_gebco_data.sh")])

def checkout_cesm(repo_url="https://github.com/CROCODILE-CESM/CESM.git", checkout_dir="cesm"):
    """
    Clone the CESM repository and run the ./bin/git-fleximod tool.

    Parameters:
    - repo_url: str, URL of the CESM Git repository.
    - checkout_dir: str, local directory to clone into.

    Raises:
    - RuntimeError if git clone or git-fleximod fails.
    """
    if not os.path.exists(checkout_dir):
        print(f"Cloning CESM from {repo_url} into {checkout_dir}...")
        result = subprocess.run(["git", "clone", repo_url, checkout_dir], check=True)
    else:
        print(f"Directory '{checkout_dir}' already exists. Skipping clone.")

    fleximod_path = os.path.join(checkout_dir, "bin", "git-fleximod")

    if not os.path.isfile(fleximod_path):
        raise RuntimeError(f"`git-fleximod` not found at {fleximod_path}")

    print("Running git-fleximod...")
    result = subprocess.run([fleximod_path], cwd=checkout_dir, check=True)

    print("CESM and git-fleximod setup complete.")

if __name__ == "__main__":
    main()