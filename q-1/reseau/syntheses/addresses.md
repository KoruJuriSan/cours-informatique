# Adresses in networking

### MAC Addr

- Physical adresses, different for every NIC.

- 6 x 4 x 2 = 48 bits
- Hexadecimal
- XX:XX:XX:XX:XX:XX


### IPv4 Addr

- Logical afresses

#### Addresse
- 4 x 8 bits = 32 bits
- Decimal/Binaire
- (0-255).(0-255).(0-255).(0-255) / xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx

#### Masque
- 4 x 8 bits = 32 bits
- Decimal/Binaire
- (0-255).(0-255).(0-255).(0-255) / xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx / (1-32)

#### Private IP range
| Prefix          | IP range                      | CIDR |
| --------------- | ----------------------------- | ---- |
| 10.0.0.0        | 10.0.0.0 - 10.255.255.255     |   /8 |
| 172.16.0.0      | 172.16.0.0 - 172.31.255.255   |  /12 |
| 192.168.0.0     | 192.168.0.0 - 192.168.255.255 |  /16 |

> |!| 127.0.0.1 (The IP a computer uses to refer to itself)

#### Class IP Range
| Classes | Subnet mask   | Network addr                |
| ------- | ------------- | --------------------------- |
| A       | 255.0.0.0     | 1.0.0.0   - 126.255.255.255 |
| B       | 255.255.0.0   | 128.0.0.0 - 191.255.255.255 |
| C       | 255.255.255.0 | 192.0.0.0 - 223.255.255.255 |
| D       | 240.0.0.0     | 224.0.0.0 - 239.255.255.255 |
| E       | -             | 240.0.0.0 - 255.255.255.255 |

### IPv6 Addr

- COOMING LATER...