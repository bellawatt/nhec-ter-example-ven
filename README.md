# NHEC TER Example Ven

The NHEC Transactive Energy Rate program communicates with devices using the [openADR](https://www.openadr.org/) communication protocol.

The core of the program is:

1. NHEC sends day-ahead energy prices to participants
2. The participant's device(s) decide their energy activity based on those prices.
3. The participant sends a report with hourly usage data for their device(s) once per day.
4. NHEC's billing system settles the account and credits the member for energy discharged into the grid.

This VEN (Virtual End Node) demonstrates the core functionality that a VEN must implement in order to participate in the program.

It uses the Python [openLEADR library](https://openleadr.org/) under the hood.

The code here could be used in two ways:

1. If you already have a VEN in development, the code can be used for initial testing and as a guide for what needs to be implemented within your system.
2. If you are implementing an openADR based system for the first time, this repo can be forked and used as the basis for a new application with the capability to participate in the NHEC TER program.

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

The communication between this VEN and the VTN follows the openADR XML based protocol, with the interactions listed in the table below.

The examples payloads are only suggestive and cannot be used as is. Many values are set dynamically by the VEN or the VTN. Any node with a value like (SOME_VALUE) indicates that this is a dynamically set field.

|Interaction|Description|VEN Payload|VTN Payload|
|-|-|-|-|
|VEN Registration|This makes the VEN known to the VTN so that it can poll for pricing events, register reports, and send reports back|[Request](example_payloads/ven_registration_request.xml)|[Response](example_payloads/ven_registration_response.xml)|
|Report Registration|The VEN will register two reports with the VTN: a `TELEMETRY_STATUS` report that reports device status and a `TELEMETRY_USAGE` report which sends hourly energy usage.|[Request](example_payloads/report_registration_request.xml)|[Response](example_payloads/report_registration_response.xml)|
|Status Report|The VEN will send a report with the status of the device. The sampling frequency and reporting interval are set by the VTN during report registration.|[Request](example_payloads/status_report_request.xml)|[Response](example_payloads/status_report_response.xml)|
|Usage Report|The VEN will send a report with dummy kWh energy usage values. The sampling frequency and reporting interval are set by the VTN during report registration. The NHEC VTN will set a sampling frequency of 1 hour and a reporting internval of once daily. In plain terms, hourly kWh data is reported once per day.|[Request](example_payloads/usage_report_request.xml)|[Response](example_payloads/usage_report_response.xml)|
|Price event polling|The VEN will poll the VTN for events. Once per day, typically around 5PM Eastern Time, the VTN will create an event that contains prices for each of the 24 hours for the following day. When the VEN polls and finds that event, it will print the data to the logs of the running VEN. The program partipant's software should respond to those prices according to the participant's preferences. That it not demonstrated in this example VEN.|[Request](example_payloads/event_polling_request.xml)|[Response](example_payloads/event_polling_response.xml)|
