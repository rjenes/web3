import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class DuneAuthenticationParameters:
    DUNE_API_KEY = os.getenv("DUNE_API_KEY")
