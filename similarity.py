#!/usr/bin/env python3
import ssdeep

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

a = "this is a test"
b = "this is a tes"

#100% similarity
print(jaccard_similarity(a,b))
