import os
from dotenv import load_dotenv

# load the env
load_dotenv()

ABSOLUTE_PATH = os.path.dirname(__file__)
RELATIVE_PATH = "sql/dev" if os.getenv("STAGE") == "development" else "sql/prod"
FULL_PATH = os.path.join(ABSOLUTE_PATH, RELATIVE_PATH)
