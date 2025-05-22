# Setup Instructions for Packet Sniffer

## 1. Install KVM and Libvirt
On the host:
```bash
sudo apt update
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
sudo systemctl enable --now libvirtd
sudo usermod -aG libvirt $(whoami)
```

## 2. Create the Isolated Network (`labnet`)
Define the `labnet` network:
```bash
sudo virsh net-define labnet.xml
sudo virsh net-start labnet
sudo virsh net-autostart labnet
sudo ip link set labnet-br2 promisc on
```

## 3. Set Up Virtual Machines
- **Kali Linux (`192.168.1.10`)**:
  - Download and install Kali Linux ISO.
  - Configure network:
    ```bash
    sudo virsh edit kali-linux
    ```
    Ensure:
    ```xml
    <interface type='network'>
      <source network='labnet'/>
      <model type='e1000'/>
    </interface>
    ```
  - Set static IP:
    ```bash
    sudo nano /etc/network/interfaces
    ```
    ```bash
    auto eth0
    iface eth0 inet static
        address 192.168.1.10
        netmask 255.255.255.0
    ```
    ```bash
    sudo systemctl restart networking
    ```
- **Ubuntu Server (`192.168.1.20`)** and **Metasploitable (`192.168.1.30`)**:
  - Similar steps, set IPs to `192.168.1.20` and `192.168.1.30`.
  - Use `<source network='labnet'/>` in their configs.

## 4. Run the Sniffer
On Kali:
```bash
sudo ip link set eth0 promisc on
sudo python3 sniffer.py
```
