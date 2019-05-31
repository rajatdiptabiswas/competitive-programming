class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
        int xLength = grid[0].length;
        int yLength = grid.length;
        
        int[] skylineTopBottom = new int[xLength];
        int[] skylineLeftRight = new int[yLength];
        
        for (int i = 0; i < yLength; i++) {
            
            for (int j = 0; j < xLength; j++) { 
                
                if (skylineTopBottom[j] < grid[i][j])
                    skylineTopBottom[j] = grid[i][j];
                
                if (skylineLeftRight[i] < grid[i][j])
                    skylineLeftRight[i] = grid[i][j];
                
            }
            
        }
        
        // debug
        // for (int x = 0; x < xLength; x++) {
        //     System.out.print(skylineTopBottom[x] + " " + skylineLeftRight[x] + "\n");
        // }
        
        int totalIncrease = 0;
        
        for (int i = 0; i < yLength; i++) {
            for (int j = 0; j < xLength; j++) { 
                totalIncrease += Math.min(skylineTopBottom[j], skylineLeftRight[i]) - grid[i][j];
            }
        }
        
        return totalIncrease;
        
    }
}