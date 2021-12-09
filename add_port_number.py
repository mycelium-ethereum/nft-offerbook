import os

from dotenv import load_dotenv
load_dotenv()

with open("docker-scripts/start_server.sh", "a") as bash_file:
    bash_file.write(os.getenv("PORT"))