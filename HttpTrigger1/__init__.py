import logging

import azure.functions as func

from testWheel.__init__ import *

from testWheel.test import *

'''
   Functions from __init__.py
'''

function_init()
print_age(21)


'''
   Functions from test.py
'''

func_test()
print_name('World')
print_test_age(34)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
