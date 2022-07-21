# Bellawatt Example Ven

## Quickstart

Create and activate a virtual environment
```bash
python3 -m venv venv
. venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run the VEN
```bash
python3 run.py
```

## Options
```bash
python3 run.py -v my.ven.id -u https://vtn-url.com/OpenADR2/Simple/2.0b -n my-ven-name
```

|Short|Long|Description|Default|
|-|-|-|-|
|-v|--ven-id|Your VEN ID|bellawatt.example.ven.123|
|-u|--vtn-url|The url of the VTN you wish to connect to|http://localhost:8000/auth-token/OpenADR2/Simple/2.0b|
|-n|--ven-name|The name of your VEN|example-ven|
