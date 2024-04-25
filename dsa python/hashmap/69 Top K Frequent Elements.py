'''347

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
#sorting hashmap by keys:
hmap = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
keys = list(hmap.keys())
keys.sort()
sortedmap = {}
for i in keys :
    sortedmap[i] = hmap[i]
# print(sortedmap)

#sorting hashmap by values:
hmap2 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
sortedmap = sorted(hmap.items(),key= lambda x:x[1])  #sorted but in list format
sortedhmap2 = dict(sortedmap)
# print(sortedhmap2)



def topKFrequent():
    nums = [1,1,1,2,2,2,2,3]
    k = 2
    map = {}
    for x in nums:
        map[x] = map.get(x,0)+1
    

# topKFrequent()