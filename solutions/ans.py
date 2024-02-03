
def does_string_have_unique_characters(ip):
    '''Implement an algo to check if a string has all unique characters.'''
    if ip is None or len(ip) > 256:
        return False
    found_list = [False for i in range(256)]
    for c in ip:
        if found_list[ord(c)]:
            return False
        else:
            found_list[ord(c)] = True
    return True

def two_strings_are_permutation(ip):
    '''Implement an algo to check if 2 strings are permutation of each other.'''
    if ip is None or len(ip) != 2 or len(ip[0]) != len(ip[1]):
        return False
    
    found_list = [0 for i in range(256)]
    for c in ip[0]:
        found_list[ord(c)] = found_list[ord(c)] + 1
    
    for c in ip[1]:
        found_list[ord(c)] = found_list[ord(c)] - 1
        if found_list[ord(c)] < 0:
            return False
    return True

def is_string_permutation_palindrome(ip):
    '''Implement an algo to check whether a permutation of given string could be a palindrome.'''
    if ip is None or type(ip) is not str:
        return False
    
    ip = ip.lower()
    
    is_odd = [False for i in range(26)]
    for c in ip:
        pos = ord(c) - ord('a')
        if pos >= 0 and pos < 25:
            is_odd[pos] = not is_odd[pos]

    found_odd = False
    print(is_odd)
    for i in is_odd:
        if i:
            if found_odd:
                return False
            else:
                found_odd = True
    return True

def is_string_one_away_from_other(ip):
    '''Implement an algo to check if given two strings are at most a character replacement or a character insertion or a character removal away from each other.'''
    if ip is None or len(ip) != 2 or abs(len(ip[0]) - len(ip[1])) > 1:
        return False

    str1 = ip[0] if len(ip[0]) > len(ip[1]) else ip[1]
    str2 = ip[1] if len(ip[0]) > len(ip[1]) else ip[0]
    len1 = len(str1)
    len2 = len(str2)
    
    ptr1 = ptr2 = 0
    print(str1,str2)
    variance_found = False
    while(ptr1 < len1 and ptr2 < len2):
        print(str1[ptr1],str2[ptr2])
        if str1[ptr1] != str2[ptr2]:
            if variance_found:
                return False
            else:
                variance_found = True
                if(len1 > len2):
                    ptr1 += 1
        ptr1 += 1
        ptr2 += 1
    return True

def compress_string_replacing_repeats_with_count(ip):
    '''Implement an algo to replace repeating continuous characters with counts.'''
    if ip is None or type(ip) is not str or len(ip) < 1:
        return ip
    
    running_count = 1
    compressed = prev_char = ip[0]
    
    for i in range(1,len(ip)):
        if(ip[i] == prev_char):
            running_count += 1
        else:
            prev_char = ip[i]
            if(running_count > 1):
                compressed += str(running_count)
                running_count = 1
            compressed += prev_char
    if running_count > 1:
        compressed += str(running_count)
        
    if(len(ip) == len(compressed)):
        compressed = ip
        
    return compressed

def rotate_matrix_by_90(ip):
    '''Implement an algo to Rotate a nXn matrix by 90 degress.'''
    if ip is None or len(ip) == 0:
        return ip
    transpose = [[ip[j][i] for j in range(len(ip))] for i in range(len(ip[0]))]
    mirror = [[transpose[i][j] for j in range(len(transpose)-1,-1,-1)] for i in range(len(transpose))]
    return mirror

def set_all_rows_and_columns_containing_0_to_0(ip):
    '''Implement an algo to Set all Rows and Columns containing a 0 element to 0.'''
    if ip is None or len(ip) == 0:
        return ip
    
    rows_with_0 = set()
    cols_with_0 = set()
    
    rows = len(ip)
    cols = len(ip[0])
    
    for i in range(rows):
        for j in range(cols):
            if(ip[i][j] == 0):
                rows_with_0.add(i)
                cols_with_0.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in rows_with_0 or j in cols_with_0:
                ip[i][j] = 0
    
    return ip

def string_substring_of_rotated_string(ip):
    '''Implement an algo to check if 2nd string is a substring of a rotated string. Can use issubtring once.'''
    if ip is None or len(ip) != 2 or len(ip[0]) < 1 or len(ip[1]) < 1:
        return False
    
    double_rotate = ip[0] + ip[0]
    if( ip[1] in double_rotate):
        return True
    return False
