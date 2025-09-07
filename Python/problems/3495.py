def agp_sum(l, r):
    if l > r:
        return 0
    total = r * pow(4, r)
    total -= pow(4,l) * (pow(4, r-l) - 1) // 3
    total -= l * pow(4, l-1)

    return total

def calc_score(li):
    l, r = li
    lg = floor(1/2 * log2(l)) + 1
    rg = floor(1/2 * log2(r)) + 1

    if lg == rg:
        g_card = r - l + 1
        total = lg * g_card
        return (total + 1)//2

    midGroupSum = agp_sum(lg+1, rg-1)

    lg_card = pow(4, lg) - l
    rg_card = r - pow(4, rg-1) + 1
    total = lg_card * lg + midGroupSum + rg_card * rg
    return (total + 1)//2
    
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
       score = sum(calc_score(query) for query in queries)
       return score
