import time


class Cluster(object):
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name
        self.cluster_nodes = []

    def add_node(self, new_node):
        self.cluster_nodes.append(new_node)

    def refresh_node_loads(self):
        print("\nRefreshing node loads...")
        for node in self.cluster_nodes:
            node.refresh_node_load()
        print("...Node refresh complete.")

    def balance(self):
        print("\nBalancing node loads...")
        average_load = self._get_node_load_average()
        (big_node, small_node) = self._get_big_and_small_nodes()
        if big_node.current_load == 0 and small_node.current_load == 0:
            print("!!! Node loads are zero ???")
            return
        while (small_node.current_load < average_load) or (
            big_node.current_load > (average_load + 1)
        ):
            # This is cheating for the sake of demo, we really want to move actual items from one node to another
            print(
                "Moving item from node {0} ({1}) to node {2} ({3}).".format(
                    big_node.node_name,
                    big_node.current_load,
                    small_node.node_name,
                    small_node.current_load,
                )
            )
            big_node.current_load -= 1
            small_node.current_load += 1
            (big_node, small_node) = self._get_big_and_small_nodes()
        # A small pause to ensure the monitor sees the balanced cluster.
        time.sleep(2)
        print("...Load balancing complete.")

    def _get_big_and_small_nodes(self):
        big = None
        small = None
        for node in self.cluster_nodes:
            if big is None:
                big = node
            else:
                if node.current_load > big.current_load:
                    big = node
            if small is None:
                small = node
            else:
                if node.current_load < small.current_load:
                    small = node
        return big, small

    def _get_node_load_average(self):
        load_total = 0
        for node in self.cluster_nodes:
            load_total += node.current_load
        return int(load_total / self.cluster_nodes.__len__())

    def dump(self):
        print('\nCluster "{0}" node status:'.format(self.cluster_name))
        for node in self.cluster_nodes:
            print(node)
