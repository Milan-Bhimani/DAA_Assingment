class Item:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.vwt = val / wt  

def fractional_knapsack(w, items):
    items.sort(key=lambda x: x.vwt, reverse=True) 
    total_value = 0.0
    for item in items:
        if item.wt <= w:
            w -= item.wt
            total_value += item.val
        else:
            total_value += item.val * w / item.wt
            break
    return total_value