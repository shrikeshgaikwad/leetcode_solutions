class Solution {
public:
    bool isSafe(vector<vector<char>>& board, int row, int col, char dig) {
        // Row check
        for (int j = 0; j < 9; j++) {
            if (board[row][j] == dig) return false;
        }
        // Column check
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == dig) return false;
        }
        // 3x3 subgrid check
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (board[i][j] == dig) return false;
            }
        }
        return true;
    }

    bool ss(vector<vector<char>>& board, int row, int col) {
        if (row == 9) return true; // solved

        int nextRow = row, nextCol = col + 1;
        if (nextCol == 9) {
            nextRow = row + 1;
            nextCol = 0;
        }

        if (board[row][col] != '.') {
            return ss(board, nextRow, nextCol);
        }

        for (char dig = '1'; dig <= '9'; dig++) {
            if (isSafe(board, row, col, dig)) {
                board[row][col] = dig;
                if (ss(board, nextRow, nextCol)) return true;
                board[row][col] = '.'; // backtrack
            }
        }
        return false;
    }

    void solveSudoku(vector<vector<char>>& board) {
        ss(board, 0, 0);
    }
};