impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut intervals = intervals.clone();        
        intervals.sort();
        let (mut cur_start, mut cur_end) = (0, -1);
        let mut result: Vec<Vec<i32>> = Vec::new();
        for inner in intervals {
            let s = inner[0];
            let e = inner[1];
            if s <= cur_end {
                cur_end = cur_end.max(e);
            }
            else {
                if cur_start <= cur_end {
                    result.push(vec![cur_start, cur_end]);
                }
                cur_start = s;
                cur_end = e;
            }
        }
        if cur_start <= cur_end {
            result.push(vec![cur_start, cur_end]);
        }
        result
    }
}