import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DuneAuthenticationParameters:
    API_KEY = os.getenv("API_KEY")
