import json
from django.core.cache import cache
from pizza_lovers.settings import EMPTY_DATA_GRAPH


class PizzaCacheMem:
    def __init__(self):
        """
        @summary: init memcached client
        """
        self.__obj_client = cache

    def update_top_voters(self, input_data):
        """
        @summary: takes data in input and write to a file
        @param input_data: dict to save
        """
        self.__obj_client.set('top_voters', input_data)

    def get_top_voters(self):
        """
        @summary: get data from cache file in byte and convert in JSON
        @return: content
        @rtype: JSON
        """
        json_data = json.dumps(EMPTY_DATA_GRAPH)

        b_top_voters = self.__obj_client.get('top_voters') or json_data

        result = json.loads(b_top_voters)

        return result
