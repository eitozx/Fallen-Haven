import os
import dotenv
dotenv.load_dotenv()

class Token:
    API = os.getenv("API_KEY")
    