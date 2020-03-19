def one_to_one_map(str1,str2):
    a = set(str1)
    b = set(str2)
    return(len(str1)==len(str2) and len(a) >= len(b) and len(a)==len(str1))



