import json
import sqlite3

from models.TestCase import TestCase

def get_test_cases(problem):
    con = sqlite3.connect("local.db")
    cur = con.cursor()
    if(problem is not None and len(problem) > 0):
        res = cur.execute("SELECT input, expected from test_cases where problem = ?", [problem])
    else:
        res = cur.execute("SELECT input, expected from test_cases")
    
    test_cases = []
    
    for row in res:
        test_cases.append(TestCase(json_or_value(row[0]), json_or_value(row[1])))
    con.close()    
    return test_cases

def json_or_value(input):
    output = input
    try:
        output = json.loads(input)
    except Exception:
        pass
    return output