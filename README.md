# NHEC TER Example Ven

The NHEC Transactive Energy Rate program communicates with devices using the [openADR](https://www.openadr.org/) communication protocol.

The core of the program is:

1. NHEC sends day-ahead energy prices to participants
2. The participant's device(s) decide whether to discharge or draw energy from the grid based on those prices
3. The participant sends a report with hourly usage data for their device(s) once per day.
4. NHEC's billing system settles the account and credits the member for energy discharged into the grid.

This VEN (Virtual End Node) demonstrates the core functionality that a VEN must implement in order to participate in the program.

It uses the Python [openLEADR library](https://openleadr.org/) under the hood.

## Prerequisites

In order to properly connect to the NHEC VTN, you need a URL which contains a token that identifies you. This is set up manually and distributed by the Bellawatt team.

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

## Interations with the VTN & example payloads

The communication between this VEN and the VTN follows the openADR XML based protocol, with the following interactions:

|Interaction|Description|VEN Payload|VTN Payload|
|-|-|-|-|
|VEN Registration|This makes the VEN known to the VTN so that it can poll for pricing events, register reports, and send reports back|||
|Report Registration|The VEN will register two reports with the VTN: a `TELEMETRY_STATUS` report that reports device status and a `TELEMETRY_USAGE` report which sends hourly energy usage.|||
|Status Report|The VEN will send a report with the status of the device. The sampling frequency and reporting interval are set by the VTN during report registration. The NHEC VTN will set a sampling frequency of [5 minutes???] and a reporting interval of [5 minutes???]|||
|Usage Report|The VEN will send a report with dummy kWh energy usage values. The sampling frequency and reporting interval are set by the VTN during report registration. The NHEC VTN will set a sampling frequency of 1 hour and a reporting internval of once daily. In plain terms, hourly kWh data is reported once per day.|||
|Price event polling|The VEN will poll the VTN for events. Once per day, typically around 5PM Eastern Time, the VTN will create an event that contains prices for each of the 24 hours for the following day. When the VEN polls and finds that event, it will print the data to the logs of the running VEN. The program partipant's software should respond to those prices according to the participant's preferences. That it not demonstrated in this example VEN.|||
