
def search(file_name, list_of_strings):
    """Get line from the file along with line numbers, which contains any string from the list"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            line_number += 1
            # For each line, check if line contains any string from the list of strings
            for string_to_search in list_of_strings:
                if string_to_search in line:
                    # If any string is found in line, then append that line along with line number in list
                    list_of_results.append((string_to_search,'Line ' + str(line_number), line.rstrip()))
    # Return list of tuples containing matched string, line numbers and lines where string is found
    return list_of_results


search_list = search('TikToks.txt',['WORDS-TO-SEARCH(COMMA SEPARATED IN LIST FORMAT)'])
for i in search_list:
    print(i)
    print('\n')