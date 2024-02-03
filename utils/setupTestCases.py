import json
import sqlite3

all_test_cases = [
        ('does_string_have_unique_characters', 'nest', True),
        ('does_string_have_unique_characters', 'meet', False),
        ('two_strings_are_permutation', json.dumps(['abcd', 'dbac']), True),
        ('two_strings_are_permutation', json.dumps(['any', 'thing']), False),
        ('two_strings_are_permutation', json.dumps(['abc', 'abcd']), False),
        ('two_strings_are_permutation', json.dumps(['Abc', 'abca']), False),
        ('two_strings_are_permutation', json.dumps(['abc', 'abca']), False),
        ('is_string_permutation_palindrome', 'some test', False),
        ('is_string_permutation_palindrome', 'taco cat', True),
        ('is_string_permutation_palindrome', 'zzAA', True),
        ('is_string_permutation_palindrome', 'z - az', True),
        ('is_string_one_away_from_other', json.dumps(['abcd', 'abc']), True),
        ('is_string_one_away_from_other', json.dumps(['any', 'thing']), False),
        ('is_string_one_away_from_other', json.dumps(['abcd', 'abcd']), True),
        ('is_string_one_away_from_other', json.dumps(['acd', 'abcd']), True),
        ('is_string_one_away_from_other', json.dumps(['abc', 'abcd']), True),
        ('compress_string_replacing_repeats_with_count', 'abcd','abcd'),
        ('compress_string_replacing_repeats_with_count', 'aabccdd','aabccdd'),
        ('compress_string_replacing_repeats_with_count', 'aaabccd','a3bc2d'),
        ('compress_string_replacing_repeats_with_count', '',''),
        ('rotate_matrix_by_90', json.dumps([]), json.dumps([])),
        ('rotate_matrix_by_90', json.dumps([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), json.dumps([[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])),
        ('rotate_matrix_by_90', json.dumps([[1,2,3],[4,5,6],[7,8,9]]), json.dumps([[7,4,1],[8,5,2],[9,6,3]])),
        ('set_all_rows_and_columns_containing_0_to_0', json.dumps([]), json.dumps([])),
        ('set_all_rows_and_columns_containing_0_to_0', json.dumps([[1,2,0,4],[5,6,7,8],[0,10,11,12],[13,14,15,16]]), json.dumps([[0,0,0,0],[0,6,0,8],[0,0,0,0],[0,14,0,16]])),
        ('set_all_rows_and_columns_containing_0_to_0', json.dumps([[1,2,3],[4,5,6],[7,8,9]]), json.dumps([[1,2,3],[4,5,6],[7,8,9]])),
        ('string_substring_of_rotated_string', json.dumps(['abcdefg', 'fga']), True),
        ('string_substring_of_rotated_string', json.dumps(['abcdefg', 'fgb']), False),
        ('string_substring_of_rotated_string', json.dumps(['abcdefg', 'cde']), True),
        ('string_substring_of_rotated_string', json.dumps(['abcdefg', 'xyz']), False),
        ('string_substring_of_rotated_string', json.dumps(['abcdefg', '']), False),
        ('string_substring_of_rotated_string', json.dumps(['', 'n']), False),
        ('remove_dupes_from_linked_list', json.dumps([]), json.dumps([])),
        ('remove_dupes_from_linked_list', json.dumps([1,2,3,4,5,4,3,7,8,9,1,11,7,23,2]), json.dumps([1,2,3,4,5,7,8,9,11,23])),
        ('remove_dupes_from_linked_list', json.dumps([1,2,3,4,5,6]), json.dumps([1,2,3,4,5,6])),
        ('find_kth_element_from_last_node_in_linked_list', json.dumps([[],0]), json.dumps([])),
        ('find_kth_element_from_last_node_in_linked_list', json.dumps([[1,2],[]]), json.dumps([])),
        ('find_kth_element_from_last_node_in_linked_list', json.dumps([[1,2,3,4,5,6],3]), 3),
        ('find_kth_element_from_last_node_in_linked_list', json.dumps([[1,2,3,4,5,6],0]), 6),
        ('find_kth_element_from_last_node_in_linked_list', json.dumps([[1,2,3,4,5,6],5]), 1),
        ('find_kth_element_from_last_node_in_linked_list', json.dumps([[1,2,3,4,5,6],8]), json.dumps([])),
        ('delete_node_from_linked_list', json.dumps([[],0]), json.dumps([])),
        ('delete_node_from_linked_list', json.dumps([[1,2],[]]), json.dumps([1,2])),
        ('delete_node_from_linked_list', json.dumps([[1,2,3,4,5,6],3]), json.dumps([1,2,4,5,6])),
        ('delete_node_from_linked_list', json.dumps([[1,2,3,4,5,6],0]), json.dumps([1,2,3,4,5,6])),
        ('delete_node_from_linked_list', json.dumps([[1,2,3,4,5,6],6]), json.dumps([1,2,3,4,5,6])),
        ('delete_node_from_linked_list', json.dumps([[1,2,3,4,5,6],8]), json.dumps([1,2,3,4,5,6])),
        ('partition_linked_list_at_value', json.dumps([[],0]), json.dumps([])),
        ('partition_linked_list_at_value', json.dumps([[1,2],[]]), json.dumps([1,2])),
        ('partition_linked_list_at_value', json.dumps([[10,2,4,1,10,5,5,6,3],4]), json.dumps([2,1,3,10,4,10,5,5,6])),
        ('partition_linked_list_at_value', json.dumps([[1,2,3,4,5,6],3]), json.dumps([1,2,3,4,5,6])),
        ('partition_linked_list_at_value', json.dumps([[5,6,7,4,3,1,2],3]), json.dumps([1,2,5,6,7,4,3])),
]

def rebuild_db():
        con = sqlite3.connect("local.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS test_cases")
        cur.execute("CREATE TABLE test_cases(problem, input, expected)")
        con.commit()
        con.close()

def add_test_cases(test_cases):
        con = sqlite3.connect("local.db")

        cur = con.cursor()
        cur.executemany("INSERT INTO test_cases VALUES(?,?,?)", test_cases)
        con.commit()
        con.close()  
        
def print_test_cases(problem):
    con = sqlite3.connect("local.db")
    cur = con.cursor()
    if(problem is not None and len(problem) > 0):
        res = cur.execute("SELECT input, expected from test_cases where problem = ?", [problem])
    else:
        res = cur.execute("SELECT input, expected from test_cases")

    for row in res:
            print(row)

    con.close()    
    
def full_db_reset():
        rebuild_db()
        add_test_cases(all_test_cases)
        print_test_cases(None)


# full_db_reset()

test_cases = [

]
add_test_cases(test_cases)
print_test_cases('partition_linked_list_at_value')