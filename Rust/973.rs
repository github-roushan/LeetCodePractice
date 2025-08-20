impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut points = points.clone();
        points.sort_by_key(|tp| tp[0]*tp[0] + tp[1]*tp[1]);
        points.into_iter().take(k as usize).collect()
    }
}