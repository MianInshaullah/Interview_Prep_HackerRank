"""
There is an array of n integers. There are also 2 disjoint sets, A and  B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, 
if i is a member of A, you add 1 to your happiness. If i is a member of B, you add -1 to your happiness. 
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

"""



if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for i in arr:
        if i in good:
            happiness += 1
        elif i in bad:
            happiness -= 1
    print(happiness)
