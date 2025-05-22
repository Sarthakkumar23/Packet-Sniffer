# Packet Sniffer and Analyzer

## Overview
This project implements a packet sniffer and analyzer to capture HTTP and FTP traffic between two virtual machines (Ubuntu Server at `192.168.1.20` and Metasploitable at `192.168.1.30`) using Kali Linux (`192.168.1.10`) on an isolated KVM network (`labnet`, `192.168.1.0/24`). The sniffer (`sniffer.py`) logs packets to `capture.log`, focusing on TCP traffic on ports 80 (HTTP) and 21 (FTP) containing `GET`, `POST`, or `USER` commands.

### Project Structure
- `sniffer.py`: Packet sniffer script (Python 3) running on Kali Linux.
- `labnet.xml`: KVM network configuration for the isolated `labnet` network.
- `setup.md`: Instructions to set up the KVM environment and VMs.
- `troubleshooting.md`: Documentation of issues faced and solutions applied.
- `requirements.txt`: Python dependencies for `sniffer.py`.
- `LICENSE`: MIT License for the project.
- `.gitignore`: Excludes unnecessary files (e.g., VM images, logs).

## Prerequisites
- KVM host with `libvirt` installed.
- Three VMs: Kali Linux, Ubuntu Server, Metasploitable.
- Python 3 on Kali Linux.
- Root privileges on Kali for raw socket access.

## Quick Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Sarthakkumar23/Packet-Sniffer-Analyzer.git
   cd Packet-Sniffer
   ```
2. Set up the KVM network and VMs (see `setup.md`).
3. Run the sniffer on Kali:
   ```bash
   sudo python3 sniffer.py
   ```
4. Generate traffic from Ubuntu:
   ```bash
   curl http://192.168.1.30
   ftp 192.168.1.30
   ```
5. Check `capture.log` for captured packets.

## Sample Output
- Sniffer Output:
  ```bash
  sudo python3 sniffer.py                
  Sniffing packets....
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  TCP Packet: 192.168.1.30:80 -> 192.168.1.20:34324
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  Payload: 
  zeGET / HTTP/1.1
  Host: 192.168.1.30
  User-Agent: curl/8.5.0
  Accept: */*

  ...
  TCP Packet: 192.168.1.30:80 -> 192.168.1.20:34324
  TCP Packet: 192.168.1.30:80 -> 192.168.1.20:34324
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  TCP Packet: 192.168.1.30:80 -> 192.168.1.20:34324
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  TCP Packet: 192.168.1.30:80 -> 192.168.1.20:34324
  TCP Packet: 192.168.1.20:34324 -> 192.168.1.30:80
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  Payload: 
  əUSER Anonymous
  ...
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  TCP Packet: 192.168.1.30:21 -> 192.168.1.20:56558
  TCP Packet: 192.168.1.20:56558 -> 192.168.1.30:21
  ^C
  stopped sniffing.
  ```
- Sample capture.log Format:
```
  192.168.1.20:34324 -> 192.168.1.30:80
  Payload: 
  GET / HTTP/1.1
  Host: 192.168.1.30
  User-Agent: curl/8.5.0
  Accept: */*



  192.168.1.20:56558 -> 192.168.1.30:21
  Payload: 
  USER Anonymous
```

## Ethical Use
This tool is for educational purposes only. Unauthorized packet sniffing is illegal and unethical. Ensure you have permission to monitor the network and comply with all applicable laws.

## License
This project is licensed under the MIT License (see `LICENSE`).

## Author
Created by Sarthak.
