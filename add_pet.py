from __future__ import print_function
import time
import swagger_client

from swagger_client.rest import ApiException
from pprint import pprint

configuration = swagger_client.Configuration()
#configuration.access_token = 'YOUR_ACCESS_TOKEN'

api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pet(id = 987000111, name="osman", status="sold",
                         photo_urls=["http://img.example.com/doggie.png"],
                         category=swagger_client.Category(id=42)) # Pet | Pet object that needs to be added to the store

try:
    # Add a new pet to the store
    pprint(api_instance.add_pet(body))
    #api_instance.find_pets_by_status(status='available')
    

except ApiException as e:
    print("Exception when calling PetApi->add_pet: %s\n" % e)