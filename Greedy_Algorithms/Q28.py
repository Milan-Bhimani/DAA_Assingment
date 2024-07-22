from collections import OrderedDict

def page_faults(pages, capacity):
    page_faults = 0
    cache = OrderedDict()

    for page in pages:
        if page not in cache:
            page_faults += 1
            if len(cache) == capacity:
                cache.popitem(last=False)
            cache[page] = None
        else:
            cache.move_to_end(page)

    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
print(page_faults(pages, capacity)) 