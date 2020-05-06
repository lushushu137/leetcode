def findMedianSortedArrays(nums1, nums2) -> float:
    nums3 = []
    while nums1 and nums2:
        a = nums1[0]
        b = nums2[0]
        if a < b:
            nums3.append(a)
            nums1.pop(0)
        else:
            nums3.append(b)
            nums2.pop(0)
    if nums1:
        nums3 += nums1
    if nums2:
        nums3 += nums2
    print(nums3)
    if len(nums3) / 2 == len(nums3) // 2:
        mid1 = nums3[len(nums3) // 2]
        mid2 = nums3[len(nums3) // 2 - 1]
        print(mid1, mid2)
        return (mid1 + mid2) / 2
    else:
        return nums3[len(nums3) // 2]


print(findMedianSortedArrays([1, 2], [3, 4]))
