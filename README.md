# Port-Service-Identifier

A Python script that identifies the common service associated with a given network port number.

## How It Works

The program stores a dictionary mapping well-known port numbers to the services that typically use them. When you enter a port number, it looks it up in the dictionary and tells you what service it's associated with.

### Recognized Ports

| Port  | Service         |
|-------|-----------------|
| 20    | FTP Data Transfer |
| 21    | FTP Control     |
| 22    | SSH             |
| 23    | Telnet          |
| 25    | SMTP            |
| 53    | DNS             |
| 80    | HTTP            |
| 110   | POP3            |
| 143   | IMAP            |
| 443   | HTTPS           |
| 3306  | MySQL           |
| 5432  | PostgreSQL      |
| 6379  | Redis           |
| 27017 | MongoDB         |

If the entered port isn't in the list, the program lets you know it's not recognized.

## How to Run

1. Make sure you have Python installed.
2. Run the script:

python port_service_identifier.py

3. Enter a port number when prompted.

## Possible Improvements

- Add more ports to the mapping (e.g. 8080, 8443, 993, 995)
- Handle non-numeric input gracefully instead of crashing
- Allow looking up multiple ports without restarting the program
- Load the port/service mapping from an external file instead of hardcoding it

