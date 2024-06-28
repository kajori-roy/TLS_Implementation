# TLS Protocol Implementation

## Overview

This project demonstrates the implementation of the TLS (Transport Layer Security) protocol to secure communication between a client and a server. The project covers the fundamental aspects of TLS, including encryption, authentication, and data integrity. There is no utilization of the inbuilt algorithms.

## Features

- **Secure Communication:** Establishes a secure connection between the client and server.
- **Encryption:** Utilizes symmetric and asymmetric encryption to protect data.
- **Authentication:** Ensures the identities of the communicating parties.
- **Data Integrity:** Verifies that data has not been tampered with during transmission.

## Implementation Details

### Components

- **Client:** Initiates the TLS handshake and communicates with the server.
- **Server:** Responds to the client and establishes a secure session.

### Steps

1. **TLS Handshake:** Establishes a secure session with the exchange of keys.
2. **Symmetric Key Encryption:** Uses a shared key for encrypting data.
3. **Asymmetric Key Encryption:** Uses public and private keys for authentication.
4. **Data Transmission:** Securely transmits data between the client and server.

### Technologies Used

- **Python:** Programming language for implementation.
- **OpenSSL:** Library for SSL/TLS protocols.

## Getting Started

### Prerequisites

- Python 3.x
- OpenSSL library

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tls-protocol-implementation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd tls-protocol-implementation
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the server:
    ```bash
    python server.py
    ```
2. Start the client:
    ```bash
    python client.py
    ```

For more details, watch the [YouTube video](https://www.youtube.com/watch?v=t8pd0N3Nz3U&t=31s). This is made by us. This youtube video has all the description on TLS and the demo run of this project

**Link to the Youtube video** 
https://www.youtube.com/watch?v=t8pd0N3Nz3U&t=31s

