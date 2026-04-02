"""
This script setups all credentials needed
"""

import os
import copernicusmarine


def main():
    setup_glorys_credentials()




def setup_glorys_credentials():
    """
    Set up the credentials for accessing the GLORYS data.
    """
    glorys_username = os.getenv("GLORYS_USERNAME")
    glorys_password = os.getenv("GLORYS_PASSWORD")

    if not copernicusmarine.login(check_credentials_valid=True):
        copernicusmarine.login(
            username=glorys_username, password=glorys_password, force_overwrite=True
        )

