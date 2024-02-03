import inspect
from flask import render_template
from models.CustomLinkedList import LinkedList, Node

from utils.localdb import get_test_cases


def execute_solution(module, function_name):
    function = getattr(module,function_name)
    
    test_cases = get_test_cases(function_name)
    
    for testable in test_cases:
        testable.set_actual(function(testable.input))
        
    return render_template('solution.html', 
                           problem_name= function_name.replace('_', ' ').capitalize(),
                           description= inspect.getdoc(function),
                           code_block= inspect.getsource(function),
                           testcases=test_cases)        
    
def linked_list_from_array(arr):
    ll = LinkedList(Node(arr[0]))
    for el in arr[1:]:
        ll.append(Node(el))
    return ll