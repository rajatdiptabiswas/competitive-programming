/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    
    let xLength = grid[0].length;
	let yLength = grid.length;

	// skylineTopBottom = new Array(xLength).fill(0);
	// skylineLeftRight = new Array(yLength).fill(0);
    
    (skylineTopBottom = []).length = xLength;
    skylineTopBottom.fill(0);
	(skylineLeftRight = []).length = yLength;
    skylineLeftRight.fill(0);

	for (let i = 0; i < yLength; i++) {
		for (let j = 0; j < xLength; j++) {

			if (skylineTopBottom[j] < grid[i][j])
                    skylineTopBottom[j] = grid[i][j];
                
            if (skylineLeftRight[i] < grid[i][j])
                skylineLeftRight[i] = grid[i][j];

		}
	}

	var totalIncrease = 0;

	for (let i = 0; i < yLength; i++) {
        for (let j = 0; j < xLength; j++) { 
            totalIncrease += Math.min(skylineTopBottom[j], skylineLeftRight[i]) - grid[i][j];
        }
    }

    return totalIncrease;
    
};