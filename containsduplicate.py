class Solution(object):
    def containsDuplicate(self, nums):
        #for every element in in list check if number matches with any one
        # create an array to store used values 
        
        arr = set()
        for i in nums: 
            if i in arr:
                return True
            arr.add(i)
        return False