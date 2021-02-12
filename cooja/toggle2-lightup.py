import logging

import sys

import asyncio

from aiocoap import *

logging.basicConfig(level=logging.INFO)

@asyncio.coroutine



def main():
	for num in range(2,8):
		   # num = str(sys.argv[1])

		    protocol = yield from Context.create_client_context()
		
		    request = Message(code=GET)
		
		    address = "coap://[cafe::c30c:0:0:" + str(num) + "]/actuators/ledstatus"
		
		    request.set_request_uri(address)
		
		    try:
		
		        response = yield from protocol.request(request).response
		
		    except Exception as e:
		
		        print('Failed to fetch resource:')
		
		        print(e)
		
		    else:
		        #print('Result: %s[barra-n]%r'%(response.code, response.payload))
		        variavel = response.payload
		        variavel = str(variavel)
		        print('\n')

		        print ('Status lâmpada ' + str(num) + ' é: ' + variavel[2:5])

		        if variavel[2:5] == 'OFF':
		        	address = "coap://[cafe::c30c:0:0:" + str(num) + "]/actuators/toggle"
		        	request = Message(code=POST)
		        	request.set_request_uri(address)
		        	try:
		        		response = yield from protocol.request(request).response
		        	except Exception as e:
		        		print('Failed to fetch resource:')
		        		print(e)
		        	else:
		        		print('Ligando lâmpada ' + str(num))

if __name__ == "__main__":

   asyncio.get_event_loop().run_until_complete(main())
