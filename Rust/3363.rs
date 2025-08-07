impl Solution {
    pub fn max_collected_fruits(fruits: Vec<Vec<i32>>) -> i32 {
        let n = fruits.len();

        let main_diag_sum: i32 = (0..n).map(|i| fruits[i][i]).sum();

        let fruit_refs: Vec<&[i32]> = fruits.iter().map(|row| row.as_slice()).collect();
        let total1 = Self::get_total_fruit_collected(&fruit_refs);

        let transposed = Self::transpose(&fruit_refs);
        let transposed_refs: Vec<&[i32]> = transposed.iter().map(|row| row.as_slice()).collect();
        let total2 = Self::get_total_fruit_collected(&transposed_refs);
        main_diag_sum + total1 + total2
    }

    fn get_total_fruit_collected(grid: &[&[i32]]) -> i32 {
        let n = grid.len();
        let mut prev = vec![i32::MIN; n];
        let mut curr = vec![i32::MIN; n];

        prev[n - 1] = grid[0][n - 1];

        for i in 1..n - 1 {
            for j in (n - i - 1).max(i + 1)..n {
                let mut best = prev[j];
                if j > 0 {
                    best = best.max(prev[j - 1]);
                }
                if j + 1 < n {
                    best = best.max(prev[j + 1]);
                }
                curr[j] = best + grid[i][j];
            }
            std::mem::swap(&mut prev, &mut curr);
        }

        prev[n - 1]
    }

    fn transpose(matrix: &[&[i32]]) -> Vec<Vec<i32>> {
        (0..matrix.len())
            .map(|j| matrix.iter().map(|row| row[j]).collect())
            .collect()
    }
}