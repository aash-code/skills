from app import app
import solutions.ll as module
from utils.render import execute_solution

@app.route("/ll/remove_dupes")
def remove_dupes():
    return execute_solution(module, "remove_dupes_from_linked_list")

@app.route("/ll/n_minus_k_element")
def n_minus_k_element():
    return execute_solution(module, "find_kth_element_from_last_node_in_linked_list")

@app.route("/ll/delete_node")
def delete_node():
    return execute_solution(module, "delete_node_from_linked_list")

@app.route("/ll/partition")
def partition():
    return execute_solution(module, "partition_linked_list_at_value")