from datetime import timedelta
from openleadr import OpenADRClient
from openleadr.enums import MEASUREMENTS
from random import random

class ExampleVen:
  """
  Example VEN based on OpenLeadr. See more docs here: https://openleadr.org/docs/client.html

  Sample Payload Representations can be found here: https://openleadr.org/docs/representations.html
  """
  def __init__(self, **kwargs):
    self.client = OpenADRClient(**kwargs)
    self.run = self.client.run

    self.register_handlers()

  def register_handlers(self):
    self.client.add_handler('on_event', self.handle_event)

    self.client.add_report(
      callback=self.energy_report,
      report_specifier_id='RealEnergy',
      measurement=MEASUREMENTS.REAL_ENERGY,
      resource_id='example-device-001',
      sampling_rate=timedelta(hours=1),
    )

    self.client.add_report(
      callback=self.status_report,
      report_specifier_id='Status',
      report_name='TELEMETRY_STATUS',
      resource_id='example-device-001',
      sampling_rate=timedelta(seconds=30),
    )

  
  @staticmethod
  async def handle_event(event):
    print('Just received an event!', event)

    for signal in event['event_signals']:
      if signal['signal_name'] == 'ELECTRICITY_PRICE' and signal['signal_type'] == 'price':
        for interval in signal['intervals']:
          print(f'Start: {interval["dtstart"].isoformat()}')
          print(f'Duration: {interval["duration"].seconds}')
          print(f'Price: {interval["signal_payload"]}')
    
    return 'optIn'

  @staticmethod
  async def energy_report():
    """
    OpenLeadr will automatically aggregate values here, so we only need
    to pass a measurement. Alternatively, you can pass a list of (datetime, value) tuples
    to process all of the report at once.

    See more here: https://openleadr.org/docs/reporting.html
    """
    return random()
  
  @staticmethod
  async def status_report():
    """
    The tuple expected is (online, manual_override, capacity). Just as with energy, a datetime value
    can be added as the first element of the tuple if you would like to determine it manually.
    """
    return (True, False, {
      'min': 0,
      'max': 10,
      'current': 5,
      'normal': 8,
    })
