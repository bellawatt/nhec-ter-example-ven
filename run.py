from asyncio import get_event_loop
from argparse import ArgumentParser
from ven import ExampleVen

VTN_URL = 'http://localhost:8000/auth-token/OpenADR2/Simple/2.0b'
VEN_ID = 'bellawatt.example.ven.123'
VEN_NAME = 'example-ven'

parser = ArgumentParser(prog='example-ven', description='Arguments for running the Example Ven')
parser.add_argument('-v', '--ven-id', type=str, default=VEN_ID, help='Your ven-id')
parser.add_argument('-u', '--vtn-url', type=str, default=VTN_URL, help='The url of the vtn you will be connecting to')
parser.add_argument('-n', '--ven-name', type=str, default=VEN_NAME, help='The name of your ven')

args = parser.parse_args()

ven = ExampleVen(
  ven_id=args.ven_id,
  ven_name=args.ven_name,
  vtn_url=args.vtn_url,
)

loop = get_event_loop()
loop.create_task(ven.run())
loop.run_forever()
