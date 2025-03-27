'''def rem(l,word):
    l.remove(word)
    return l
l=["bhavesh","yash","darshan","lokesh"]
print(rem(l, "lokesh"))'''

def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n


l=["bhavesh","yash","darshan","lokesh"]
print(rem(l, "sh"))

 