struct MergeSorted<'a> {
    nums1: &'a [i32],
    nums2: &'a [i32],
    p1: usize,
    p2: usize,
}

impl<'a> MergeSorted<'a> {
    fn new(nums1: &'a [i32], nums2: &'a [i32]) -> Self {
        MergeSorted { nums1, nums2, p1: 0, p2: 0 }
    }
}

impl<'a> Iterator for MergeSorted<'a> {
    type Item = i32;

    fn next(&mut self) -> Option<Self::Item> {
        let n = self.nums1.len();
        let m = self.nums2.len();

        if self.p1 < n && self.p2 < m {
            if self.nums1[self.p1] < self.nums2[self.p2] {
                self.p1 += 1;
                Some(self.nums1[self.p1 - 1])
            } else {
                self.p2 += 1;
                Some(self.nums2[self.p2 - 1])
            }
        } else if self.p1 == n && self.p2 < m {
            self.p2 += 1;
            Some(self.nums2[self.p2 - 1])
        } else if self.p2 == m && self.p1 < n {
            self.p1 += 1;
            Some(self.nums1[self.p1 - 1])
        } else {
            None
        }
    }
}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let mut merged_iter = MergeSorted::new(&nums1, &nums2);
        let n: usize = nums1.len();
        let m: usize = nums2.len();
        if (n+m) % 2 == 1 {
            let target_ind = (n+m)/2;
            merged_iter.nth(target_ind).unwrap() as f64
        }
        else {
            let target_ind = (n+m)/2  - 1;
            let a = merged_iter.nth(target_ind).unwrap() as f64;
            let b = merged_iter.next().unwrap() as f64;
            (a as f64 + b as f64) / 2.0
        }
    }
}