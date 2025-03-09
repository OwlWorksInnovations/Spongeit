import paramiko
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Execute commands over SSH")
    parser.add_argument("-ip", "--server", required=True, help="Server IP address")
    parser.add_argument("-u", "--username", default="spongeit", help="SSH username")
    parser.add_argument("-pass", "--password", required=True, help="SSH password")
    parser.add_argument("-c", "--command", default="ls -la", help="Command to execute")
    
    # Parse arguments
    args = parser.parse_args()

    # Intialize
    client = paramiko.SSHClient()

    # Automatically adds the server's host keys
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connects using username and password
    client.connect(args.server, username=args.username, password=args.password)

    try:
        # Execute a command
        stdin, stdout, stderr = client.exec_command(args.command)
    
        # Read the output
        output = stdout.read().decode()
        error = stderr.read().decode()
    
        print("Output:")
        print(output)
    
        if error:
            print("Errors:")
            print(error)
        
    finally:
        # Always close the connection when done
        client.close()

if __name__ == "__main__":
    main()
