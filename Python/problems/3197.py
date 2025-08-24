from typing import List
from dataclasses import dataclass
import copy

@dataclass
class Rect:
    rs: int
    cs: int
    re: int
    ce: int

    def area(self):
        L = max(0, self.re - self.rs + 1)
        B = max(0, self.ce - self.cs + 1)
        return L*B

inf = 1000000
NULL_RECT = Rect(inf ,inf,-inf, -inf)

def bounding_box(grid, rect):
    resulting_rect = copy.deepcopy(NULL_RECT)
    if not (0 <= rect.rs and rect.re < len(grid)):
        return resulting_rect
    if not (0 <= rect.cs and rect.ce < len(grid[0])):
        return resulting_rect

    for i in range(rect.rs, rect.re+1):
        for j in range(rect.cs, rect.ce+1):
            if grid[i][j] == 0:
                continue
            resulting_rect.rs = min(resulting_rect.rs, i)
            resulting_rect.re = max(resulting_rect.re, i)
            resulting_rect.cs = min(resulting_rect.cs, j)
            resulting_rect.ce = max(resulting_rect.ce, j)
    
    return resulting_rect

def do_vertical_split(rect, col_ind):
    if col_ind < rect.cs:
        return copy.deepcopy(NULL_RECT), rect
    if rect.ce < col_ind:
        return rect, copy.deepcopy(NULL_RECT)
    
    left_rect = Rect(rect.rs, rect.cs, rect.re, col_ind)
    right_rect = Rect(rect.rs, col_ind+1, rect.re, rect.ce)

    return left_rect, right_rect

def do_horizontal_split(rect, row_ind):
    if row_ind < rect.rs:
        return copy.deepcopy(NULL_RECT), rect
    if rect.re < row_ind:
        return rect, copy.deepcopy(NULL_RECT)
    
    top_rect = Rect(rect.rs, rect.cs, row_ind, rect.ce)
    bottom_rect = Rect(row_ind+1, rect.cs, rect.re, rect.ce)

    return top_rect, bottom_rect

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        result = inf
        grid_box = Rect(0,0,R-1, C-1)
        
        for c1 in range(C):
            l_rect, r_rect = do_vertical_split(grid_box, c1)
            area_left = bounding_box(grid, l_rect).area()
            area_right = bounding_box(grid, r_rect).area()

            for c2 in range(c1+1, C):
                lr_rect, rr_rect = do_vertical_split(r_rect, c2)
                area2 = bounding_box(grid, lr_rect).area()
                area3 = bounding_box(grid, rr_rect).area()
                result = min(result, area_left + area2 + area3)
            
            for r1 in range(R):
                tr_rect, br_rect = do_horizontal_split(r_rect, r1)
                area2 = bounding_box(grid, tr_rect).area()
                area3 = bounding_box(grid, br_rect).area()                
                result = min(result, area_left + area2 + area3)
                
                tl_rect, bl_rect = do_horizontal_split(l_rect, r1)
                area2 = bounding_box(grid, tl_rect).area()
                area3 = bounding_box(grid, bl_rect).area()
                result = min(result, area_right + area2 + area3)

        for r1 in range(R):
            t_rect, b_rect = do_horizontal_split(grid_box, r1)
            area_top = bounding_box(grid, t_rect).area()
            area_bottom = bounding_box(grid, b_rect).area()

            for r2 in range(r1+1, R):
                bt_rect, bb_rect = do_horizontal_split(b_rect, r2)
                area2 = bounding_box(grid, bt_rect).area()
                area3 = bounding_box(grid, bb_rect).area()
                result = min(result, area_top + area2 + area3)

            for c1 in range(C):
                lt_rect, rt_rect = do_vertical_split(t_rect, c1)
                area2 = bounding_box(grid, lt_rect).area()
                area3 = bounding_box(grid, rt_rect).area()
                result = min(result, area_bottom + area2 + area3)
                
                lb_rect, rb_rect = do_vertical_split(b_rect, r1)
                area2 = bounding_box(grid, lb_rect).area()
                area3 = bounding_box(grid, rb_rect).area()
                result = min(result, area_top + area2 + area3)
            
        return result
