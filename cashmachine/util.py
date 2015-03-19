def check_dict_keys(keys, dict_var):
    result = all([k in dict_var and dict_var.get(k) is not None for k in keys])
    if not result:
        raise KeyError
