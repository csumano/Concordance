# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_concordance import (
    ResultConcordance,
)  # noqa: F401,E501
from swagger_server import util


class Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, concordance: List[ResultConcordance] = None, input: str = None
    ):  # noqa: E501
        """Result - a model defined in Swagger

        :param concordance: The concordance of this Result.  # noqa: E501
        :type concordance: List[ResultConcordance]
        :param input: The input of this Result.  # noqa: E501
        :type input: str
        """
        self.swagger_types = {"concordance": List[ResultConcordance], "input": str}

        self.attribute_map = {"concordance": "concordance", "input": "input"}
        self._concordance = concordance
        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> "Result":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def concordance(self) -> List[ResultConcordance]:
        """Gets the concordance of this Result.


        :return: The concordance of this Result.
        :rtype: List[ResultConcordance]
        """
        return self._concordance

    @concordance.setter
    def concordance(self, concordance: List[ResultConcordance]):
        """Sets the concordance of this Result.


        :param concordance: The concordance of this Result.
        :type concordance: List[ResultConcordance]
        """
        if concordance is None:
            raise ValueError(
                "Invalid value for `concordance`, must not be `None`"
            )  # noqa: E501

        self._concordance = concordance

    @property
    def input(self) -> str:
        """Gets the input of this Result.


        :return: The input of this Result.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input: str):
        """Sets the input of this Result.


        :param input: The input of this Result.
        :type input: str
        """
        if input is None:
            raise ValueError(
                "Invalid value for `input`, must not be `None`"
            )  # noqa: E501

        self._input = input