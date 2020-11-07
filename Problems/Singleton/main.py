# Truthy values
one = 1
one = bool(one)
non_empty_string = "singleton"
non_empty_string = bool(non_empty_string)
# Falsy values
zero = 0
empty_list = []
zero = bool(zero)
empty_list = bool(empty_list)
# NoneType
none_obj = None
