import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    def __init__(self):
        self.base_url = 'https://api.deepseek.com'
        self.api_key = os.getenv('DEEPSEEK_API_KEY')
        self.model_name = 'deepseek-v4-flash'