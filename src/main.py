import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path='../credentials/.env')

def main():
    print('Welcome to GENESIS!')
    print('System initialized successfully!')

if __name__ == '__main__':
    main()
