impl Solution {
    pub fn is_trionic(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let p = Self::get_ind(&nums, 0, true);
        if p>=n-2 || p == 0 {
            return false;
        }
        let q = Self::get_ind(&nums, p, false);
        if q >= n-1 {
            return false;
        }
        Self::get_ind(&nums, q, true) == n
    }

    pub fn get_ind(nums: &Vec<i32>, cur_ind: usize, increasing: bool) -> usize {
        let n = nums.len();
        for i in cur_ind..n-1 {
            if (increasing && nums[i] >= nums[i+1]) || (!increasing && nums[i] <= nums[i+1]) {
                return i;
            }
        }
        n
    }
}