"""
Dynamodb database connection and queriees
"""
import boto3

class Database:
    """ Queries for dynamodb """
    @staticmethod
    def put(body, result, table):
        """ Put an item into the table """

        dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
        table = dynamodb.Table(table)

        table.put_item(Item={"body": body, "concordance": result})

    @staticmethod
    def check_key(body, table):
        """ Check an item """
        dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
        table = dynamodb.Table(table)

        item = table.get_item(Key={"body": body})
        return item

    @staticmethod
    def get_item(body, table):
        """ Get a item """
        dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
        table = dynamodb.Table(table)

        item = table.get_item(Key={"body": body})
        return item
