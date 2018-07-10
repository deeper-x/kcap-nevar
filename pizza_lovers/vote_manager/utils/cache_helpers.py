from pizza_lovers.settings import CACHE_FILE, DEFAULT_LABEL
import os
import json


class PizzaCache:
    def __init__(self):
        self._cache_file_path = os.getcwd() + CACHE_FILE
        self.__init_file()

    def __init_file(self):
        """
        @summary: if cache file is not present, creates one
        """
        if not os.path.isfile(self._cache_file_path):
            data = {"names": [DEFAULT_LABEL], "votes": [0]}
            json_data = json.dumps(data)

            with open(self._cache_file_path, 'w') as empty_file:
                json.dump(json_data, empty_file)

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



