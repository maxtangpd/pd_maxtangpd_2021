import sys
def one_to_one_map(str1,str2):
    a = set(str1)
    b = set(str2)
    print(len(str1)==len(str2) and len(a) >= len(b) and len(a)==len(str1))

one_to_one_map(sys.argv[1],sys.argv[2])
