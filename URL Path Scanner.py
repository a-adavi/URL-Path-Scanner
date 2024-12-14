import requests

def scan_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found: {url}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    # Get input file and target URL from the user
    input_file = input("Please enter the input file name: ")
    target_url = input("Please enter the target URL example https://googl.com/: ")

    # Read common paths from the file
    with open(input_file, 'r') as file:
        common_paths = file.readlines()

    # Remove extra characters like \n
    common_paths = [path.strip() for path in common_paths]

    for path in common_paths:
        full_url = target_url + path
        scan_url(full_url)
