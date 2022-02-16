# larenga.py

# def pascal(n, k):
#     if n < 2:
#         return 1
    
#     p_list = []
    
#     while len(p_list) < n + 1:
#         p_list2 = p_list.copy()
#         p_list = [1]
#         while len(p_list2) > 1:
#             p_list.append(p_list2.pop(0) + p_list2[0])
#         p_list.append(1)
        
#     return p_list[k]

# [1]+[p.pop(0) + p[0] for e in p]+[p.pop(0) + p[0] for e in p]+[1]

def pascal(n, k = 0):
    if n < 2:
        return 1
    
    def _pascal(p_list):
        if len(p_list) > n:
            return p_list
        
        def __pascal(r, p = []):
            if len(r) > 1:
                p.append(r.pop(0) + r[0])
                return __pascal(r, p)
            return [1] + p + [1]
        
        return _pascal(__pascal(p_list))
            
    
    p_list = _pascal([1,1])
    
    return p_list[k]