import csv
from datetime import datetime
import json

import numpy as np


filepath = "data.csv"

class MiFitnessData:
    def __init__(self, path):
        self.path = path
        self.data = self.loadcsv()
        self.keys = self.get_keys()

    def loadcsv(self) -> np.array:
        with open(self.path, 'r') as f:
            data = list(csv.reader(f, delimiter=","))
        return np.array(data[1::])

    def filter_key(self, key: str) -> np.array:
        filtered_data = []
        for row in self.data:
            if str(row[2]) == key:
                filtered_data.append(row)
        return np.array(filtered_data)

    def get_keys(self) -> np.array:
        keys = []
        for row in self.data:
            if str(row[2]) not in keys:
                keys.append(str(row[2]))

        return np.array(keys)


mi = MiFitnessData(filepath)
print(mi.data)
print(mi.filter_key("heart_rate"))
print(mi.keys)

