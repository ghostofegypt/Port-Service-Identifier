def port_service_identifier():
    port_service_mapping = {
        20: "FTP Data Transfer",
        21: "FTP Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        5432: "PostgreSQL",
        6379: "Redis",
        27017: "MongoDB"
    }

    user_input = input("Enter a port number: ")

    if not user_input.isdigit():
        print("Invalid input. Please enter a numeric port number.")
        return

    port_number = int(user_input)

    if port_number in port_service_mapping:
        print(f"Port {port_number} is used for {port_service_mapping[port_number]}.")
    else:
        print(f"Port {port_number} is not recognized in the mapping.")

port_service_identifier()
