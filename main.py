from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

name = os.getenv("NAME")
# password = os.getenv("NAUKRI_PASSWORD")

print(name)