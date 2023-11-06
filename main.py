def binary(s,b):
    s=bin(s)
    if s.startswith('-'):
        s=s[s.index('b')+1:]
        if len(s)!=b:
            s=(b-len(s))*'0'+s
        s='1'+s
        return s
    s=s[s.index('b')+1:]
    if len(s)!=b:
        s=(b-len(s))*'0'+s
    return s
binary(s,b)
