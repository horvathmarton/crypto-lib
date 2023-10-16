# Crypto Lib

A comprehensive Python library for simplifying the debugging of cryptographic challenges in Capture The Flag (CTF) competitions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the Crypto Lib, a CTF-focused Python library designed to assist security enthusiasts and CTF teams in debugging and analyzing cryptographic challenges effectively. Whether you're a seasoned CTF player or just getting started, this library will make your life easier.

Currently we support AES and RSA builing blocks, so if you have a challenge where you found the vulnerability they can help you to debug your solution easier.

## Getting Started

To get started with Crypto Lib, follow these simple steps:

1. Clone the repository:

```bash
git clone https://github.com/horvathmarton/cryptolib.git
```

2. Install the required dependencies

```bash
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

3. Start using the library in your Python projects:

```python
import cryptolib

# Example usage:
plaintext = cryptolib.decrypt_aes(encrypted_text, key)
```

## Usage

The Crypto Lib offers a range of functions and tools for debugging cryptographic challenges. Refer to the documentation for detailed usage examples and API documentation.

## Contributing

We welcome contributions from the CTF community. To contribute to Crypto Lib, please follow our contribution guidelines.

## License
Crypto Lib is licensed under the MIT License. You are free to use, modify, and distribute this library for personal and commercial use.

If you have any questions, issues, or suggestions, please open an issue. We appreciate your feedback and support!
