# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.result import Result  # noqa: E501
from swagger_server.models.result2 import Result2  # noqa: E501
from swagger_server.test import BaseTestCase

class TestAnalysisController(BaseTestCase):
    """AnalysisController integration test stubs"""

    #Test case 1, get_concordance endpoint, Standard input POST
    def test_get_concordance(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/analyze",
            method="POST",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 2, get_concordance endpoint, int ipnut POST
    def test_get_concordance_t2(self):
        """Test case for get_concordance

        Calculate
        """
        body = 222
        response = self.client.open(
            "/csumano/Concordance/1.0.0/analyze",
            method="POST",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 3, get_concordance endpoint, empty input POST to invalid endpoint (error 404)
    def test_get_concordance_t3(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"Test"'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/doesNotExist",
            method="POST",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert404(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 4, get_concordance endpoint, empty input POST
    def test_get_concordance_t4(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/analyze",
            method="GET",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 5, get_concordance endpoint, empty input PUT
    def test_get_concordance_t5(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/analyze",
            method="PUT",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 6, get_concordance endpoint, empty input DELETE
    def test_get_concordance_t6(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/analyze",
            method="DELETE",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 7, get_concordance endpoint, empty input POST as HTML
    def test_get_concordance_t7(self):
        """Test case for get_concordance_v2

        Calculate and locate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/analyze",
            method="POST",
            data=json.dumps(body),
            content_type="text/html",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))






    #Test case 1, get_concordance_v2 endpoint, Standard input POST
    def test_get_concordance_v2(self):
        """Test case for get_concordance_v2

        Calculate and locate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="POST",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 2, get_concordance_v2 endpoint, Empty input POST
    def test_get_concordance_v2_t2(self):
        """Test case for get_concordance

        Calculate
        """
        body = '""'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="POST",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 3, get_concordance_v2 endpoint, int input POST
    def test_get_concordance_v2_t3(self):
        """Test case for get_concordance

        Calculate
        """
        body = 32
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="POST",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 4, get_concordance_v2 endpoint, Standard input GET
    def test_get_concordance_v2_t4(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="GET",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 5, get_concordance_v2 endpoint, Standard input PUT
    def test_get_concordance_v2_t5(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="PUT",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))


    #Test case 6, get_concordance_v2 endpoint, Standard input DELETE
    def test_get_concordance_v2_t6(self):
        """Test case for get_concordance

        Calculate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="DELETE",
            data=json.dumps(body),
            content_type="text/plain",
        )
        self.assert405(response, "Response body is : " + response.data.decode("utf-8"))

    #Test case 7, get_concordance_v2 endpoint, Standard input DELETE text/html
    def test_get_concordance_v2_t7(self):
        """Test case for get_concordance_v2

        Calculate and locate
        """
        body = '"The brown fox jumped over the brown log."'
        response = self.client.open(
            "/csumano/Concordance/1.0.0/locate",
            method="POST",
            data=json.dumps(body),
            content_type="text/html",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
