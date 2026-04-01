# Health Check Script

import requests
import time

# Configuration
HEALTH_CHECK_URL = 'http://example.com/health'

# Function to perform health check

def health_check():
    try:
        response = requests.get(HEALTH_CHECK_URL)
        return response.status_code == 200
    except Exception as e:
        print(f'Error during health check: {e}')
        return False

# Main loop

def main():
    while True:
        if health_check():
            print('Service is healthy')
        else:
            print('Service is unhealthy')
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    main()