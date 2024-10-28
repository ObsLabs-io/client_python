# coding: utf-8

"""
    ObsLabs API

    # Authentication  ObsLabs uses basic auth to authenticate the API. You can create API keys in the account settings. Use your API key as the basic auth password. The username should be left blank (notice the colon sign before api-key that must be included). All requests must be made over https.  Example usage: ```bash curl -u :<YOUR API KEY> https://api.obslabs.io/v1/users/me ```  # Errors  The API returns a structured error response in case of failure. Below is the format of the error response object:  ```json {   \"error\": {     \"status\": 400,     \"code\": \"VALIDATION\",     \"message\": \"Validation errors occurred.\",     \"details\": [       {         \"field\": \"email\",         \"issue\": \"The email address is not in a valid format.\"       },       {         \"field\": \"password\",         \"issue\": \"The password must be at least 8 characters long.\"       }     ]   } } 

    The version of the OpenAPI document: 1.0
    Contact: contact@obslabs.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "obslabs-api"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="ObsLabs API",
    author="OpenAPI Generator community",
    author_email="contact@obslabs.io",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "ObsLabs API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    # Authentication  ObsLabs uses basic auth to authenticate the API. You can create API keys in the account settings. Use your API key as the basic auth password. The username should be left blank (notice the colon sign before api-key that must be included). All requests must be made over https.  Example usage: &#x60;&#x60;&#x60;bash curl -u :&lt;YOUR API KEY&gt; https://api.obslabs.io/v1/users/me &#x60;&#x60;&#x60;  # Errors  The API returns a structured error response in case of failure. Below is the format of the error response object:  &#x60;&#x60;&#x60;json {   \&quot;error\&quot;: {     \&quot;status\&quot;: 400,     \&quot;code\&quot;: \&quot;VALIDATION\&quot;,     \&quot;message\&quot;: \&quot;Validation errors occurred.\&quot;,     \&quot;details\&quot;: [       {         \&quot;field\&quot;: \&quot;email\&quot;,         \&quot;issue\&quot;: \&quot;The email address is not in a valid format.\&quot;       },       {         \&quot;field\&quot;: \&quot;password\&quot;,         \&quot;issue\&quot;: \&quot;The password must be at least 8 characters long.\&quot;       }     ]   } } 
    """,  # noqa: E501
    package_data={"obslabs_client": ["py.typed"]},
)
