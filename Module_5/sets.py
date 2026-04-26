# my_set = {1, 2, 3, 4, 5, "hello", 7, 8, 9}
# print(23 in my_set)
# my_set.add(2)
# # is_available = "True" if x in my_set else "False"
# print(23 in my_set)
# print((my_set))


# admins = {"alice", "bob", "charlie"}
# developers = {"bob", "david", "alice"}

# print(developers ^ admins)
# print(admins - developers)


# raw_data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 4, 5, 7, 8, 34, 4, 3, 2, 43, 5, 1, 2, 4, 5, 6, 7, 4, 3, 2, 1, 4, 5, 6, 7, 8, 4, 3, 2, 3, 4]
# simplified_data = list(set(raw_data))
# print(simplified_data) 


def process_tags(user_input: list) -> list:
    # 1. Clean whitespace and lowercase everything
    clean_input = [tag for tag in user_input]
    
    # 2. Remove duplicates but KEEP the user's preferred order
    unique_tags = list(dict.fromkeys(clean_input))
    
    return unique_tags

# Usage
raw_tags =  [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 4, 5, 7, 8, 34, 4, 3, 2, 43, 5, 1, 2, 4, 5, 6, 7, 4, 3, 2, 1, 4, 5, 6, 7, 8, 4, 3, 2, 3, 4]
final_tags = process_tags(raw_tags)

print(final_tags)
# Output: ['python', 'coding', 'programming']
