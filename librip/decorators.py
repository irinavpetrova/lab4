def print_result(func):
    def decorated(*args):
        print(func.__name__)
        result = func(*args)
        if isinstance(result, dict):
            for k, v in result.items():
                print(str(k) + '=' + str(v))
        elif isinstance(result, list):
            for a in result:
                print(a)
        else:
            print(result)
        return result
    return decorated
