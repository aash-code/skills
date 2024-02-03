from app import app
import solutions.ans as module
from utils.render import execute_solution


@app.route("/ans/unique_chars_in_string")
def string_has_unique_characters():
    return execute_solution(module, "does_string_have_unique_characters")

@app.route("/ans/two_string_permutation")
def two_string_permutation():
    return execute_solution(module, "two_strings_are_permutation")

@app.route("/ans/palindrome_permutation")
def palindrome_permutation():
    return execute_solution(module, "is_string_permutation_palindrome")

@app.route("/ans/one_away")
def one_away():
    return execute_solution(module, "is_string_one_away_from_other")

@app.route("/ans/string_compression")
def string_compression():
    return execute_solution(module, "compress_string_replacing_repeats_with_count")

@app.route("/ans/rotate_matrix_by_90")
def rotate_matrix_by_90():
    return execute_solution(module, "rotate_matrix_by_90")

@app.route("/ans/zero_matrix")
def zero_matrix():
    return execute_solution(module, "set_all_rows_and_columns_containing_0_to_0")

@app.route("/ans/rotated_substring")
def rotated_substring():
    return execute_solution(module, "string_substring_of_rotated_string")