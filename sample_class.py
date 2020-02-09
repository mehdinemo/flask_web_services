import pandas as pd
from datetime import datetime


class SampleClass:
    def __init__(self, test_string, core_numbers):
        self.test_string = test_string
        self.core_numbers = core_numbers

    def method1(self, nodes: pd.DataFrame, edges: pd.DataFrame, epsilon: float) -> dict:
        results = {"nodes_number": len(nodes), "edges_numbers": len(edges), "core_numbers": self.core_numbers,
                   "epsilon": epsilon}
        return results

    def print_test(self, test_string: str) -> str:
        message = test_string + "\t" + str(datetime.now())
        return message
