import json
import pkg_resources


def json_graph(model):
    json_dict = {}

    # build links json representation
    json_dict["links"] = []
    for s_node, t_node in model.links_:
        link_dict = {"source" : str(s_node),
                     "target" : str(t_node),
                     "value"  : 1 }
        json_dict["links"].append(link_dict)

    # node json representation
    json_dict["nodes"] = []
    for (p_n, p) in enumerate(model.nodes_):
        for (c_n, c) in enumerate(p):
            node_dict = {"id" : str((p_n, c_n)),
                         "group" : 1,
                         "color" : 1 } 
            json_dict["nodes"].append(node_dict)

    return json.dumps(json_dict, indent=4)

def html_graph(model):

    resource_package = __name__ 
    resource_path = '/'.join(['graph_template.html'])
    template = pkg_resources.resource_string(resource_package, resource_path)
    json_graph_str = json_graph(model)
    template_pars = {"title" : "default title",
                     "width" :  400,
                     "height" : 400,
                     "json_graph" : json_graph_str,
                     "graph_charge" : -120,
                     "graph_link_distance" : 30,
                     "graph_gravity" : 0.1 }
    return template.format(**template_pars)
