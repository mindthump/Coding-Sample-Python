#!/usr/bin/env python

import monitorlog
import cluster
import node
import monitor
import threading


def main():
    cluster_node_qty = 5
    cluster_name = "primary"
    current_cluster = cluster.Cluster(cluster_name)

    # Add 1 to index to make the name and IP a little nicer
    for new_node_id in range(1, cluster_node_qty + 1):
        current_cluster.add_node(node.Node('node-%s' % new_node_id, '10.0.0.%s' % new_node_id))
    print('Cluster "{0}" populated with {1} nodes.'.format(cluster_name, cluster_node_qty))

    mlog = monitorlog.MonitorLog()
    cluster_monitor = monitor.Monitor(current_cluster, mlog)
    monitor_thread = threading.Thread(target=cluster_monitor.start_monitoring)
    monitor_thread.start()
    print('Monitor started.')

    current_cluster.refresh_node_loads()
    current_cluster.dump()

    current_cluster.balance()
    current_cluster.dump()

    current_cluster.refresh_node_loads()
    current_cluster.dump()

    current_cluster.balance()
    current_cluster.dump()

    cluster_monitor.stop()
    monitor_thread.join()

    mlog.dump()


if __name__ == "__main__":
    main()
