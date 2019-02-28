import random
import time


class Node(object):
    def __init__(self, node_name, ipaddress):
        self.node_name = node_name
        self.ipaddress = ipaddress
        # This is set when the loads are refreshed; it could be replaced by a collection of load items (e.g., users)
        self.current_load = 0

    def refresh_node_load(self):
        min_load = 0
        max_load = 20
        self.current_load = random.randint(min_load, max_load)
        print(
            "Refreshed node {0} to load {1}".format(self.node_name, self.current_load)
        )
        time.sleep(1)

    def __str__(self):
        return "Node {0} IP = {1} Load = {2}".format(
            self.node_name, self.ipaddress, self.current_load
        )
