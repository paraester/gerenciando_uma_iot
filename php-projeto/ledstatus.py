import logging

import sys

import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

@asyncio.coroutine



def main():

    num = str(sys.argv[1])

    protocol = yield from Context.create_client_context()

    request = Message(code=GET)

    address = "coap://[cafe::c30c:0:0:" + num + "]/actuators/ledstatus"

    request.set_request_uri(address)

    try:

        response = yield from protocol.request(request).response

    except Exception as e:

        print('Failed to fetch resource:')

        print(e)

    else:

        print('Result: %s[barra-n]%r'%(response.code, response.payload))

if __name__ == "__main__":

   asyncio.get_event_loop().run_until_complete(main())
