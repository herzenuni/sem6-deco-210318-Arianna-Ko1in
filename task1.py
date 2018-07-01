import hashlib

def gethash(value):
    th = hashlib.sha256()
    th.update(str(value).encode("iso-8859-1"))
    return th.hexdigest()

def tohash(f):
    if type(f) is str:
        return gethash(f)
    elif type(f) is dict:
        for key in f.keys():
            f[key] = gethash(f[key])
        return f
    elif type(f) in (set,frozenset,tuple,list):
        newset = []
        for data in f:
            newset.append(gethash(data))
        if type(f) is tuple:
            return tuple(newset)
        elif type(f) is list:
            return list(newset)
        else:
            return set(newset)

stringhash = tohash("Hello")
assert stringhash, "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
print(stringhash)

listsource = [1,2,3]
listhash = tohash(listsource)
assert(type(listhash) is list)
assert(len(listhash)==len(listsource))
print(listhash)

tuplesource = (4,5,6)
tuplehash = tohash(tuplesource)
assert(type(tuplehash) is tuple)
assert(len(tuplehash)==len(tuplesource))
print(tuplehash)

dictsource = {"a":1, "b":2}
dicthash = tohash(dictsource)
assert(type(dicthash) is dict)
assert(len(dicthash)==len(dictsource))
print(dicthash)

setsource = set([7,8,9])
sethash = tohash(setsource)
assert(type(sethash) is set)
assert(len(sethash)==len(setsource))
print(sethash)
