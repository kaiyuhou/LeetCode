You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

### 题意

给定一个方阵，顺时针旋转90度
要求原地实现

### 题解

我就是死算的

disucss给了一种更聪明的方法
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}