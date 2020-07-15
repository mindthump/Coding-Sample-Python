import datetime
import time

# this is intended to be run in a thread. However, python threads don't have a termination method,
# so we put a "stop" method in the class to set a flag that we check periodically (i.e., with each log action)
class Monitor(object):
    def __init__(self, cluster, monitor_log):
        self._running = True
        self._cluster = cluster
        self._monitor_log = monitor_log

    def stop(self):
        self._running = False

    def start_monitoring(self):
        # do some counting
        while self._running:
            self.check_nodes()
            time.sleep(1)

    def check_nodes(self):
        for node in self._cluster.cluster_nodes:
            self._monitor_log.add_entry(
                node.node_name,
                node.ipaddress,
                datetime.datetime.now(),
                node.current_load,
            )
