from datetime import timedelta
from openleadr import OpenADRClient
from random import random

def example_report_value():
  return random()

class ExampleVen:
  def __init__(self, **kwargs):
    self.client = OpenADRClient(**kwargs)
    self.run = self.client.run

    self.register_handlers()

  def register_handlers(self):
    self.client.add_handler('on_event', self.handle_event)

    self.client.add_report(
      callback=example_report_value,
      report_specifier_id='RealEnergy',
      resource_id='example-device-001',
      measurement='voltage',
      sampling_rate=timedelta(seconds=10),
    )

  @staticmethod
  async def handle_event(event):
    print('Just received an event!', event)
