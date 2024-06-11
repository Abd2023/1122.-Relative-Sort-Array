class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        hashmap =  {}

        for item in arr1:
            hashmap[item] = hashmap.get( item, 0) + 1

        result = []
        for item in arr2:
            result.extend( [item] * hashmap[item])
            hashmap.pop(item)

        remaining = []
        for num in hashmap:
            for _ in range(hashmap[num]):
                remaining.append(num)
        
        
        remaining.sort()

        result.extend(remaining)
        
        return result
        
        


        
