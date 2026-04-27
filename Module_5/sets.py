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


# def process_tags(user_input: list) -> list:
#     # 1. Clean whitespace and lowercase everything
#     clean_input = [tag for tag in user_input]
    
#     # 2. Remove duplicates but KEEP the user's preferred order
#     unique_tags = list(dict.fromkeys(clean_input))
    
#     return unique_tags

# # Usage
# raw_tags =  [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 4, 5, 7, 8, 34, 4, 3, 2, 43, 5, 1, 2, 4, 5, 6, 7, 4, 3, 2, 1, 4, 5, 6, 7, 8, 4, 3, 2, 3, 4]
# final_tags = process_tags(raw_tags)

# print(final_tags)
# # Output: ['python', 'coding', 'programming']





# def process_tags(user_input: list) -> list:
#     # 1. Convert to string, clean whitespace, and lowercase
#     # This handles both numbers and strings safely
#     clean_input = [str(tag).strip().lower() for tag in user_input]
    
#     # 2. Remove duplicates while keeping order
#     unique_tags = list(dict.fromkeys(clean_input))
    
#     return unique_tags

# # Use strings if that is your intended final output format
# raw_tags = [" Python ", "coding", "PYTHON", "Programming", "coding"]
# final_tags = process_tags(raw_tags)

# print(final_tags) 
# # Output: ['python', 'coding', 'programming']

# print(f"There is a ")




# import sys

# mylist= [1, 2, 3, 4, "Hello"]
# my_tuple = (1, 2, 3, 4, "Hello")
# my_set = {1, 2, 3, 4, "Hello"}

# print(f"{sys.getsizeof(my_tuple)}")
# print(f"{sys.getsizeof(mylist)}")
# print(f"{sys.getsizeof(my_set)}")


# Example: Using a frozenset to map a combination of ingredients to a recipe
# ingredients = frozenset(['flour', 'sugar', 'eggs'])
# recipes = {ingredients: "Basic Cake"}

# # You can look it up with a new frozenset containing the same items
# search_key = frozenset(['sugar', 'eggs', 'flour'])
# print(recipes[search_key])  # Output: Basic Cake




# normal_set = {1, 2, 3, 4}
# normal_set.add(5)
# forzen = frozenset([1, 2, 3, 4, 5])
# print(type(normal_set))
# print(normal_set)
# print(type(forzen))



# dict = {
# frozenset({1, 2, 3}) : "Admin"
# }
# print(dict[frozenset({1, 2, 3})])

# key1 = frozenset([1, 2, 3, 4])
# key2 = frozenset([2, 1, 4, 3, 2, 1])

# print(key1 == key2)


# sets = {1, 2, 3, 4, 5}
# sets.add(7)
# sets.clear()
# print(sets)
set1 = {1, 2, 3, 4}
set2 = {2, 3, 4}
print(set1.difference_update(set2))