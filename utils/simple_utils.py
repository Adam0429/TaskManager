def str_dict(origin_dict):
    result_dict = {}
    for key in origin_dict:
        if origin_dict[key] != None:
            result_dict[key] = str(origin_dict[key])
        else:
            result_dict[key] = ''
    return result_dict