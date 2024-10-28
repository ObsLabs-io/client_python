# coding: utf-8

"""
    ObsLabs API

    # Authentication  ObsLabs uses basic auth to authenticate the API. You can create API keys in the account settings. Use your API key as the basic auth password. The username should be left blank (notice the colon sign before api-key that must be included). All requests must be made over https.  Example usage: ```bash curl -u :<YOUR API KEY> https://api.obslabs.io/v1/users/me ```  # Errors  The API returns a structured error response in case of failure. Below is the format of the error response object:  ```json {   \"error\": {     \"status\": 400,     \"code\": \"VALIDATION\",     \"message\": \"Validation errors occurred.\",     \"details\": [       {         \"field\": \"email\",         \"issue\": \"The email address is not in a valid format.\"       },       {         \"field\": \"password\",         \"issue\": \"The password must be at least 8 characters long.\"       }     ]   } } 

    The version of the OpenAPI document: 1.0
    Contact: contact@obslabs.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from obslabs_client.models.v1_create_api_key201_response import V1CreateApiKey201Response

class TestV1CreateApiKey201Response(unittest.TestCase):
    """V1CreateApiKey201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CreateApiKey201Response:
        """Test V1CreateApiKey201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CreateApiKey201Response`
        """
        model = V1CreateApiKey201Response()
        if include_optional:
            return V1CreateApiKey201Response(
                api_key = obslabs_client.models.api_key_model.ApiKeyModel(
                    id = '', 
                    key = '', 
                    last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return V1CreateApiKey201Response(
                api_key = obslabs_client.models.api_key_model.ApiKeyModel(
                    id = '', 
                    key = '', 
                    last_used = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )
        """

    def testV1CreateApiKey201Response(self):
        """Test V1CreateApiKey201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()