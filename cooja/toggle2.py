import logging

import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

@asyncio.coroutine

def main():

    protocol = yield from Context.create_client_context()

    request = Message(code=POST)

    request.set_request_uri('coap://[cafe::c30c:0:0:3]/actuators/toggle')

    try:

        response = yield from protocol.request(request).response

    except Exception as e:

        print('Failed to fetch resource:')

        print(e)

    else:

        print('Alternando')

if __name__ == "__main__":

   asyncio.get_event_loop().run_until_complete(main())
