from asyncio import get_event_loop
from argparse import ArgumentParser
from ven import ExampleVen
import openleadr
import logging
openleadr.enable_default_logging(level=logging.DEBUG)

VTN_URL = 'http://localhost:8000/auth-token/OpenADR2/Simple/2.0b'
VEN_ID = 'bellawatt.example.ven.123'
VEN_NAME = 'example-ven'
RESOURCE_ID = 'example-device-001'

parser = ArgumentParser(prog='example-ven', description='Arguments for running the Example Ven')
parser.add_argument('-v', '--ven-id', type=str, default=VEN_ID, help='Your ven-id')
parser.add_argument('-u', '--vtn-url', type=str, default=VTN_URL, help='The url of the vtn you will be connecting to')
parser.add_argument('-n', '--ven-name', type=str, default=VEN_NAME, help='The name of your ven')
parser.add_argument('-r', '--resource-id', type=str, default=RESOURCE_ID, help='An ID for your device (known as resource in openADR)')

args = parser.parse_args()

ven = ExampleVen(
  ven_id=args.ven_id,
  ven_name=args.ven_name,
  vtn_url=args.vtn_url,
  resource_id=args.resource_id
)

loop = get_event_loop()
loop.create_task(ven.run())
loop.run_forever()
