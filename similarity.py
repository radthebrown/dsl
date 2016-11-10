#!/usr/bin/env python
import ssdeep

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)


a = "this is a test"
b = "this is a tes"
print(jaccard_similarity(a,b))
