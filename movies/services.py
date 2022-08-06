import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv()


def get_Movies():

    movies = requests.get('https://demo.credy.in/api/v1/maya/movies/', auth=HTTPBasicAuth(str(os.getenv('user_name')), str(os.getenv('pass_word'))))

    list = movies.json()

    return list
