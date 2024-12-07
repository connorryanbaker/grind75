from typing import List

def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    def merge(emails):
        curr = emails
        swaps = True
        while swaps:
            next_g = []
            swaps = False
            skip_idx = set()
            for i, email_list in enumerate(curr):
                if i in skip_idx:
                    continue
                cel = email_list
                for j, sub in enumerate(curr[i+1:]):
                    if len(set(cel) & set(sub)) > 0:
                        cel = list(set(cel + sub))
                        swaps = True
                        skip_idx.add(j + i + 1)
                next_g.append(sorted(list(set(cel))))
            curr = next_g
        return curr
                
    lookup = {}
    for a in accounts:
        name = a[0]
        curr_email_list = a[1:]
        if name in lookup:
            lookup[name].append(curr_email_list)
        else:
            lookup[name] = [curr_email_list]
    
    res = []
    for k in lookup:
        lookup[k] = merge(lookup[k])
        for el in lookup[k]:
            res.append([k] + el)
    
    return res
