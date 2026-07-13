class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)

        while l <= r:
            cut1 = (l + r) // 2
            cut2 = (len(nums1) + len(nums2) + 1) // 2 - cut1

            l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1]     if cut1 < len(nums1) else float('inf')
            l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2]     if cut2 < len(nums2) else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = cut1 - 1
            else:
                l = cut1 + 1