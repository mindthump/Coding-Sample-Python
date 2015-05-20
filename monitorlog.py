class MonitorLog(object):
    def __init__(self):
        self.log = []

    # Note: if there were potentially more than one monitor thread, the add_entry() method would need locks.
    def add_entry(self, node_name, node_ip, timestamp, current_load):
        self.log.append(_LogEntry(node_name, node_ip, timestamp, current_load))

    def dump(self):
        print('\n\nMONITOR LOG:')
        for logentry in self.log:
            print(str(logentry))


class _LogEntry(object):
    def __init__(self, node_name, node_ip, timestamp, current_load):
        self.node_name = node_name
        self.node_ip = node_ip
        self.timestamp = timestamp
        self.current_load = current_load

    def __str__(self):
        return '{0} || Node {1} IP = {2} Load = {3}'.format(self.timestamp, self.node_name, self.node_ip,
                                                            self.current_load)
