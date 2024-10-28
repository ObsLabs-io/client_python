# ObsLabs API Client for Python

## Requirements.

Python 3.7+

## Getting Started

In your own code, to use this library to connect and interact with obslabs-api,
you can run the following:

```python
import obslabs_client
from obslabs_client.rest import ApiException
from pprint import pprint

configuration = obslabs_client.Configuration(
    username = "",
    password = "API_TOKEN"
)

with obslabs_client.ApiClient(configuration) as api_client:
    api_instance = obslabs_client.UsersApi(api_client)

    try:
        api_response = api_instance.v1_my_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->v1_my_user: %s\n" % e)
```
