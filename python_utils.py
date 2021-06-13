def for_dict(d):
    for k,v in d:
        print(k)
        if  isinstance(v,list):
            for_dict(enumerate(v))
        elif isinstance(v,dict):
            for_dict(v.items())

if __name__ == '__main__':
    ob = {"a": 1, "b": [{"aa":1},{"bb":2}],"c":{"cc":11}}
    for_dict(ob.items())