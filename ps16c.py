from os import listdir, sys
from os.path import isfile, join, basename
import multiprocessing
import networkx as nx


def get_file_paths(root):
    file_paths = []
    for f in listdir(root):
        if isfile((join(root, f))):
            file_paths.append(join(root, f))
    return file_paths

def get_max_component(graph):
    components = nx.connected_component_subgraphs(graph)
    return components.next()

def job(file_path):
    file_name = basename(file_path)
    g = nx.read_edgelist(file_path)
    giant_component = get_max_component(g)


if __name__=="__main__":

    fb_folder = sys.argv[1]
    fb_file_paths = sorted(get_file_paths(fb_folder))

    if len(sys.argv) > 3:
        start_point = int(sys.argv[2])
        end_point = int(sys.argv[3])
        fb_file_paths = fb_file_paths[start_point:end_point]

    p = multiprocessing.Pool(multiprocessing.cpu_count() - 2)
    p.map(job, fb_file_paths)
