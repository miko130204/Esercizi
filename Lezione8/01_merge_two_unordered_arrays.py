import unittest

def merge(nums1, m, nums2, n):
    nums1_tmp = nums1.copy()
    i = 0 
    j = 0
    k = 0
    while i < m and j < n:
        if nums1_tmp[i] <= nums2[j]:
            nums1[k] = nums1_tmp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1

    while i < m:
        nums1[k] = nums1_tmp[i]
        i += 1
        k += 1

class TestMergeFunction(unittest.TestCase):

    def test_case_1(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,2,3,5,6])

    def test_case_2(self):
        nums1 = [1,0,0,0]
        nums2 = [2,3,4]
        merge(nums1, 1, nums2, 3)
        self.assertEqual(nums1, [1,2,3,4])

    def test_case_3(self):
        nums1 = [4,5,6,0,0,0]
        nums2 = [1,2,3]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,3,4,5,6])

    def test_case_4(self):
        nums1 = [1,2,3,0,0,0,0]
        nums2 = [0,2,2,6]
        merge(nums1, 3, nums2, 4)
        self.assertEqual(nums1, [0,1,2,2,2,3,6])

    def test_case_5(self):
        nums1 = [1,1,1,0,0]
        nums2 = [1,1]
        merge(nums1, 3, nums2, 2)
        self.assertEqual(nums1, [1,1,1,1,1])

    def test_case_6(self):
        nums1 = [2,0]
        nums2 = [1]
        merge(nums1, 1, nums2, 1)
        self.assertEqual(nums1, [1,2])

    def test_case_7(self):
        nums1 = [0]
        nums2 = [1]
        merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [1])

    def test_case_8(self):
        nums1 = [1,2,3,0,0,0]
        nums2 = []
        merge(nums1, 3, nums2, 0)
        self.assertEqual(nums1, [1,2,3,0,0,0])

    def test_case_9(self):
        nums1 = [0,0,0]
        nums2 = [1,2,3]
        merge(nums1, 0, nums2, 3)
        self.assertEqual(nums1, [1,2,3])

    def test_case_10(self):
        nums1 = [1,3,5,7,0,0,0,0]
        nums2 = [2,4,6,8]
        merge(nums1, 4, nums2, 4)
        self.assertEqual(nums1, [1,2,3,4,5,6,7,8])

if __name__ == '__main__':
    unittest.main()
