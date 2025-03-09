# **Spongeit**

**Spongeit** is a CLI tool that allows developers to offload the compilation and execution of their code to a remote server. This tool is particularly useful for developers who have a slower laptop but a more powerful server to perform intensive builds. By sending their project files to the server, the tool can compile and run code in various languages (such as C++, Python, and Rust) inside isolated Docker containers and send back the results.

---

## **How It Works**

1. **File Transfer via SFTP**  
   You send your source code and project files from your local machine to the server using SFTP.

2. **Language-Specific Build Process**  
   Once the server receives the files, it automatically detects the specified language and triggers the corresponding build process:
   - **C++ (`-l cpp`)**: Runs `make` to build the project.
   - **Python (`-l py`)**: Executes the script using `python <file_name.py>`.
   - **Rust (`-l rust`)**: Runs `cargo build --release` to compile the project.

3. **Isolated Environment via Docker**  
   The build process happens inside a Docker container, ensuring that the build environment is isolated and consistent. This allows for easy management of dependencies and ensures compatibility across different machines.

4. **Return the Results**  
   After the build process is complete, the server sends the compiled files or execution output back to the client. This allows you to continue your work without waiting for long compilation times.

---

## **Installation**

To use **spongeit**, you need to have the following installed on both your local machine and server:

1. **Python 3.13+**  
2. **Docker**  
3. **SFTP Access to the Server**

### **Client Installation**

On your local machine (the laptop or development environment):

1. Clone the repository:
   ```sh
   git clone https://github.com/OwlWorksInnovations/Spongeit.git
   cd spongeit
   ```

2. Install required Python dependencies:
   ```sh
   pip install paramiko
   ```

## **Usage**

Once installed, you can use spongeit via the command line.

### **Command Syntax**

```sh
spongeit -l <language> -d <local_project_path> -ip <server_ip> -p <port> -pass <password>
```

### **Options**

| Option | Description | Default |
|--------|-------------|---------|
| `-l <language>` | The programming language used for the project (cpp, py, rust, etc.). | Required |
| `-d <local_project_path>` | The local path to the project directory to be transferred. | Required |
| `-ip <server_ip>` | The IP address of the remote server. | Required |
| `-p <port>` | The SFTP port. | 192 |
| `-pass <password>` | The password (or use SSH key authentication). | Required |

### **Example**

To send a C++ project to a remote server for building, use the following command:

```sh
spongeit -l cpp -d /path/to/local/project -ip 192.168.0.13 -p 192 -pass mypassword
```

## **Server Setup**

1. **Docker Setup**  
   For the server to build code in isolated environments, Docker must be installed. You'll need to create Docker images for each language (C++, Rust, Python) as defined in the `dockerfiles/` directory.

2. **SFTP Server**  
   The server must have an SFTP server running (such as OpenSSH or vsftpd) to receive files from the client. Ensure that the server is configured to listen on port 192 (or change the port to match your setup).

3. **Start the Server**  
   Run the server script on your Ubuntu server to listen for incoming file transfers and trigger the build process:
   ```sh
   python3 spongeit-server/server.py
   ```

## **Project Structure**

```
spongeit/
├── spongeit-client/       # Client-side CLI tool  
│   ├── spongeit.py        # Python script for the CLI  
├── spongeit-server/       # Server-side code  
│   ├── server.py          # Python script to listen for SFTP transfers and trigger builds  
├── dockerfiles/           # Docker images for different languages (C++, Python, Rust)  
├── README.md              # This file  
```

## **Contributing**

Feel free to contribute to spongeit! If you have an idea for a new feature, a bug fix, or any other improvements, open an issue or submit a pull request.

## **License**

This project is licensed under the MIT License – see the LICENSE file for details.
