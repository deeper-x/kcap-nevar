from pizza_lovers.settings import CACHE_FILE
import os
import json


class PizzaCache:
    def __init__(self):
        self._cache_file_path = os.getcwd() + CACHE_FILE

    def update_top_voters(self, input_data):
        """
        @summary: takes data in input and write to a file
        @param input_data: dict to write into file
        """
        with open(self._cache_file_path, 'w') as cache_file:
            json.dump(input_data, cache_file)

    def get_top_voters(self):
        """
        @summary: get data from cache file in JSON
        @return: file content
        @rtype: JSON
        """
        with open(self._cache_file_path) as cache_file:
            str_data = json.load(cache_file)

            json_data = json.loads(str_data)

            return json_data



