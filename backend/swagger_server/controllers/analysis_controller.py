"""
Endpoints for analyzing user input, checks database and store in if
it is already in it
"""

from swagger_server.models.result import Result  # noqa: E501
from swagger_server.models.result2 import Result2  # noqa: E501
from swagger_server.database import Database

import botocore

def get_concordance(body=None):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: Result
    """
    # if connexion.request.is_json:
    #     body = str.from_dict(connexion.request.get_json())  # noqa: E501

    # Keep original string
    orignal_body = body.decode()

    # Try to access a dynamodb table
    try:
        test_key = Database.check_key(orignal_body, "concordance")

        if "Item" in test_key:
            item = Database.get_item(orignal_body, "concordance")
            return Result(item, orignal_body)

    except:
        print("database not found")

    # Sort string into list
    body = body.decode()
    body = body.split()
    body = [w.strip(",:;.!?").lower() for w in body]
    body.sort()

    # Create concordance list and dictionary
    conc_list = []
    conc_dict = {}

    for word in body:
        if word in conc_dict:
            conc_dict[word] += 1
        else:
            conc_dict[word] = 1

    for key, value in conc_dict.items():
        temp_dic = {}
        temp_dic["count"] = value
        temp_dic["token"] = key
        conc_list.append(temp_dic)

    result = Result(conc_list, orignal_body)

    # Try to access a dynamodb table
    try:
        Database.put(orignal_body, conc_list, "concordance")
    except:
        print("database not found")

    return result


def get_concordance_v2(body=None):  # noqa: E501
    """Calculate and locate

    Post text to generate concordance and location # noqa: E501

    :param body: Text to be analyzed and located
    :type body: dict | bytes

    :rtype: Result2
    """
    # if connexion.request.is_json:
    #     body = str.from_dict(connexion.request.get_json())  # noqa: E501

    # Keep original string
    orignal_body = body.decode()

    # Try to access a dynamodb table
    try:
        test_key = Database.check_key(orignal_body, "location")

        if "Item" in test_key:
            item = Database.get_item(orignal_body, "location")
            return Result(item, orignal_body)
    except:
        print("database not found")

    # Sort string into list
    body = body.decode()
    body = body.split()

    body = [w.strip(",:;.!?").lower() for w in body]

    location = {}

    for i, number in enumerate(body):
        location[number] = location.get(number, [])
        location[number].append(i)

    body.sort()

    conc_list = []
    word_list = []
    for word in body:
        if word not in word_list:
            word_list.append(word)
            temp_dic = {}
            temp_dic["location"] = location[word]
            temp_dic["token"] = word
            conc_list.append(temp_dic)

    result = Result2(conc_list, orignal_body)

    # Try to access a dynamodb table
    try:
        Database.put(orignal_body, conc_list, "location")
    except:
        print("database not found")

    return result
