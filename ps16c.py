from os import listdir, stat, sys
from os.path import isfile, join, basename
import time
import multiprocessing
import json
import networkx as nx
from sklearn.utils.graph import graph_shortest_path as gsp


def get_file_paths(root):
    file_paths = []
    for f in listdir(root):
        if isfile((join(root, f))):
            file_paths.append(join(root, f))
    return file_paths

def get_max_component(graph):
    """
    pass the giant component
    """
    components = nx.connected_component_subgraphs(graph)
    return components.next()

def get_gsp(component):
    """
    calulate shortest path for all vertices
    """
    am = nx.adjacency_matrix(component)
    return gsp(am, directed=False)

def get_summary(name, gsp_vals, giant_n, gn):
    """
    generate summary result
    """
    gsp_vals = gsp_vals[gsp_vals != 0]
    summary = {}
    total = gsp_vals.sum()
    number = len(gsp_vals)
    maximum = gsp_vals.max()
    mean = gsp_vals.mean()
    summary[name] = {"number": number, "total": total,
                     "max": maximum, "mean": mean,
		     "giant_component_n": giant_n, "network_size": gn}
    return summary

def to_json(data, file_name):
    json.dump(data, open(file_name, "w"))

def job(file_path):
    file_name = basename(file_path)
    print ">>> Doing: " + file_name
    start_time = time.time()

    """
    sequence)

    create graph from text file
    get the giant component
    get the giant component size
    the network size
    shortest paths for the giant component
    """
    g = nx.read_edgelist(file_path)
    giant_component = get_max_component(g)
    giant_n = len(giant_component)
    gn = len(g)
    gsp_vals = get_gsp(giant_component)

    summary = get_summary(file_name, gsp_vals)
    statinfo = stat(file_path)
    output_path = join("out", file_name + ".summary.json")
    to_json(summary, output_path)
    elapsed_time = time.time() - start_time

    print "<<< Done : " + file_name
    print "size: " + str(statinfo.st_size) + " time: %f" % elapsed_time

if __name__=="__main__":

    fb_folder = sys.argv[1]
    fb_file_paths = sorted(get_file_paths(fb_folder))

    if len(sys.argv) > 3:
        start_point = int(sys.argv[2])
        end_point = int(sys.argv[3])
        fb_file_paths = fb_file_paths[start_point:end_point]

    p = multiprocessing.Pool(multiprocessing.cpu_count() - 2)
    p.map(job, fb_file_paths)
