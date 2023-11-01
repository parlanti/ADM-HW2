import pandas as pd
import time
import json
from collections import Counter

start_time = time.time()

chunks = pd.read_json("list.json", lines = True, chunksize = 100)

tag_counter = Counter()

for chk in chunks:
    tag_lists = chk['tags'].tolist()
    
    # tag_list is a list of lists, so we have to concatenate them.
    # We had to put an if statement in the list comprehension because
    # some items are not lists but float64 variables
    tag_list = [item.lower() for lst in tag_lists for item in (lst if hasattr(lst, '__iter__') else str(lst))]    
    
    tag_counter.update(tag_list)

print("The top 5 most frequently used tags are:\n")
for elem in tag_counter.most_common(5):
    print(f"\t{elem[0]: <15}  :  {elem[1]} times")
    
execution_time = time.time() - start_time
print(f"\nExecution time: {round(execution_time)} seconds")
