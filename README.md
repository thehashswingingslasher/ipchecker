# IP Checker

This Python script takes a domain name as input and returns the corresponding IP address. The script uses the `socket` library to resolve the domain name into an IP address.

## Features

- Takes a domain name (e.g., "www.example.com") as input.
- Resolves the domain name to its corresponding IP address.
- Displays the domain name and its resolved IP address.

## Prerequisites

- Python 3.x
- No additional libraries are needed, as the `socket` module is included in the standard Python library.

## How to Run

1. Ensure that Python 3.x is installed on your system.
2. Save the script as a `.py` file, e.g., `domain_to_ip.py`.
3. Open your terminal or command prompt.
4. Run the script by typing:

   ```bash
   python domain_to_ip.py
   ```

5. You will be prompted to enter a domain name. For example:
   ```
   Enter a domain name: www.example.com
   ```

6. The script will display the domain name and its IP address:
   ```
   Domain Name: www.example.com
   IP Address: 93.184.216.34
   ```

## Example

```bash
Enter a domain name: www.google.com
Domain Name: www.google.com
IP Address: 142.250.72.132
```

## Code Explanation

- `hostname = input('Enter a domain name: ')`: Prompts the user to enter a domain name.
- `ip_add = socket.gethostbyname(hostname)`: Uses the `gethostbyname` method from the `socket` module to resolve the domain name to an IP address.
- `print(f'Domain Name: {hostname}')`: Prints the domain name entered by the user.
- `print(f'IP Address: {ip_add}')`: Prints the resolved IP address.
