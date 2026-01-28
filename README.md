# Simple Port Scanner

A basic Python port scanner. It's a simple learning project to understand how port scanning works.

## What It Does

Scans a target host to find which TCP ports are open.

## Requirements

Just Python 3.6+ (no external libraries needed)

## How to Use

Basic command:
```bash
python port_scanner.py localhost
```

Scan a specific range:
```bash
python port_scanner.py localhost -s 1 -e 1000
```

Available options:
- `-s` - start port (default: 1)
- `-e` - end port (default: 1024)
- `-t` - timeout in seconds (default: 1.0)
- `-v` - verbose mode (shows closed ports too)

## Note

This is a learning exercise. Only scan systems you own or have permission to test.
