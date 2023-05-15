from typing import Dict

import numpy as np
import json



##############################################################################
# JSON functions
##############################################################################
def print_json(jd, prefix = ''):
    if isinstance(jd, dict):
        for k, v in jd.items():
            if isinstance(v, dict) or isinstance(v, list):
                print(prefix, f"{str(k)}: ")
                print_json(v, prefix+'  ')
            elif isinstance(v, np.ndarray):
                print(prefix, f"{k}: {type(v)}, shape: ({v.shape}")
            else:
                print(prefix, k, f": {str(v)}")
    elif isinstance(jd, list):
        for v in jd:
            print_json(v, prefix+'- ')
    elif isinstance(jd, np.ndarray):
        print(prefix, f"{type(jd)}, shape: ({jd.shape}")
    else:
        print(prefix, str(jd))


def prune_json(jd: Dict, current_depth: int = 0, max_depth: int = -1):
    """
    Prune json dict to make easier to print and structure.

    * Replaces numpy ndarray with a type and shape string.
    * Allow for setting a maz depth of the tree, replacing children with '...'

    :param jd: json dictionary
    :param current_depth:
    :param max_depth:
    :return:
    """
    if isinstance(jd, dict):
        changes = dict()
        for k, v in jd.items():
            if isinstance(v, np.ndarray):
                changes[k] = f"{type(v)} shape: ({v.shape}"
            elif isinstance(v, list) or isinstance(v, dict):
                if max_depth == current_depth:
                    changes[k] = "..."
        jd |= changes
        for k, v in jd.items():
            if isinstance(v, list) or isinstance(v, dict):
                prune_json(v, current_depth+1, max_depth)

    elif isinstance(jd, list):
        changes = list()
        # Replace unwanted values
        for v in jd:
            if isinstance(v, np.ndarray):
                changes.append(f"{type(v)} shape: ({v.shape}")
            elif isinstance(v, list) or isinstance(v, dict):
                if max_depth == current_depth:
                    changes.append("...")
            else:
                changes.append(None)
        for i, v in enumerate(changes):
            if v is None:
                continue
            jd[i] = v

        # Recurse
        for v in jd:
            if isinstance(v, list) or isinstance(v, dict):
                prune_json(v, current_depth+1, max_depth)



def write_fig_tree(fig, file_path, max_depth=-1, prune_path = None):
    pj = fig.to_plotly_json()
    if prune_path is not None:
        for v in prune_path:
            pj = pj[v]

    prune_json(pj, max_depth=max_depth)

    json_object = json.dumps(pj, indent=2)
    with open(file_path, "w") as outfile:
        outfile.write(json_object)


