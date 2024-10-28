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

from obslabs_client.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_v1_create_project(self) -> None:
        """Test case for v1_create_project

        Create Project
        """
        pass

    def test_v1_delete_project(self) -> None:
        """Test case for v1_delete_project

        Delete Project
        """
        pass

    def test_v1_get_project(self) -> None:
        """Test case for v1_get_project

        Get Project
        """
        pass

    def test_v1_list_projects(self) -> None:
        """Test case for v1_list_projects

        List Projects
        """
        pass

    def test_v1_project_member_create(self) -> None:
        """Test case for v1_project_member_create

        Add Project Member
        """
        pass

    def test_v1_project_member_delete(self) -> None:
        """Test case for v1_project_member_delete

        Delete Project Member
        """
        pass

    def test_v1_project_member_update(self) -> None:
        """Test case for v1_project_member_update

        Update Project Member
        """
        pass

    def test_v1_update_project(self) -> None:
        """Test case for v1_update_project

        Update Project
        """
        pass


if __name__ == '__main__':
    unittest.main()
