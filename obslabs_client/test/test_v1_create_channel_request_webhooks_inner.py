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

from obslabs_client.models.v1_create_channel_request_webhooks_inner import V1CreateChannelRequestWebhooksInner

class TestV1CreateChannelRequestWebhooksInner(unittest.TestCase):
    """V1CreateChannelRequestWebhooksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CreateChannelRequestWebhooksInner:
        """Test V1CreateChannelRequestWebhooksInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CreateChannelRequestWebhooksInner`
        """
        model = V1CreateChannelRequestWebhooksInner()
        if include_optional:
            return V1CreateChannelRequestWebhooksInner(
                name = '012',
                url = ''
            )
        else:
            return V1CreateChannelRequestWebhooksInner(
                name = '012',
                url = '',
        )
        """

    def testV1CreateChannelRequestWebhooksInner(self):
        """Test V1CreateChannelRequestWebhooksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
