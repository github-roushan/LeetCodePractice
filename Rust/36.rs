use std::collections::HashSet;

impl Solution {
    fn is_distinct(row: &Vec<char>) -> bool {
        let filtered: Vec<char> = row.iter()
            .filter(|&&c| c!='.')
            .cloned()
            .collect();
        let set: HashSet<char> = filtered.clone().into_iter().collect();

        return set.len() == filtered.len();
    }

    fn get_column(board: &Vec<Vec<char>>, col: usize) -> Vec<char>{
        board.iter()
            .map(|row| row[col])
            .collect()
    }

    fn get_box(board: &Vec<Vec<char>>, i: usize, j: usize, l: usize, b: usize) -> Vec<char>{
        let mut result = Vec::new();
        let R = board.len();
        if R == 0 {
            return result;
        }
        let C = board[0].len();
        for di in 0..l{
            let ni = i + di;
            if ni >= R {
                break;
            }
            for dj in 0..b {
                let nj = j + dj;
                if nj >= C {
                    break;
                }
                result.push(board[ni][nj]);
            }
        }
        return result;
    }

    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        for row in &board {
            let status = Solution::is_distinct(&row);
            if status == false {
                return status;
            }
        }

        for col_ind in 0..board.len() {
            let col = Solution::get_column(&board, col_ind);
            let status = Solution::is_distinct(&col);
            if status == false {
                return status;
            }
        }

        for i in (0..9).step_by(3) {
            for j in (0..9).step_by(3) {
                let box_data = Solution::get_box(&board, i, j, 3, 3);
                let status = Solution::is_distinct(&box_data);
                if status == false {
                    return status;
                }
            }
        }
        true
    }
}