import os

from dotenv import load_dotenv

from app import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv()

app = create_app()
