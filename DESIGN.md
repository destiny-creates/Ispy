# ISpy Design structure and purpose
### Created by: destiny-creates
### Contributors: arcad3luke

## File Structure
```
Ispy/
│
├── core/
│   ├── controller.py
│   ├── config.py
│   ├── output.py
│   ├── logging.py
│   └── plugins.py
│
├── modules/
│   ├── whois.py
│   ├── nmap.py
│   └── nuclei.py
│
├── config/
│   ├── setup.py
│   └── settings.ini
│
└── main.py
```

## Scanner Flow
```
Target -> OSINT -> Nmap -> Nuclei -> Output -> Logging -> Plugins
```


## Configuration
- Store credentials in ```settings.ini```
  - Discord Webhooks
  - Target information
- Make a wrapper to seamlessly integrate calls across the scanners.
- 

## OSINT module (whois)
- Find and resolve hosting provider
- Log that node for use throughout tool

## Nmap scan (Using node from OSINT)
- Conduct a comprehensive scan that details:
  - Full host fingerprinting
    - You can't understand what you don't know
  - Vulnerabilities found
    - we can use the intel here to better understand the target and what alternative routes are possible.
  - Telemetry for network classification
    - Useful for timing checks to validate network issues, should any arise.

## Nuclei scan (Using intel from Nmap scan)
- Conduct a vulnerability scan
  - If any vulnerabilities are found, log them.
- Format output for ease of use
  - Put output in ```vulnerabilities_<target>.json```
  - Print data as a table for readability
    - Vulnerabilities based on severity and classification
    - exploit.db findings (if any)
      - Prompt user for authorization to download PoC.
      - Store PoC for static analysis later