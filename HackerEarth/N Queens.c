#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 4

int i, j;

void display(int board[N][N])
{
	int i, j;

	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			printf("%d ", board[i][j]);
		}

		printf("\n");
	}
}

bool isSafe(int board[N][N], int row, int col)
{
	// //check left horizontally
	// for(i = 0; i < col; i++)
	// {
	// 	if(board[row][i] == 1)
	// 		return false;
	// }

	//check up vertically
	for(i = 0; i < row; i++)
	{
		if(board[i][col])
			return false;
	}

	//check upper left diagonal
	for(i = 0, j = 0; i < col && j < row; i++, j++)
	{
		if(board[i][j])
			return false;
	}

	return true;
}

bool nQueens(int board[N][N], int row)
{
	if(row >= N)
		return true;

	int i;
	for(i = 0; i < N; i++)
	{
		if(isSafe(board, row, i))
		{
			board[row][i] = 1;
			
			if(nQueens(board, row+1))
			{
				return true;
			}
		}

		board[row][i] = 0;
	}

	return false;
}

int main()
{
	// int N;
	// scanf("%d", &N);

	int board[N][N];

	for(i = 0; i < N; i++)
	{
		for(j = 0; j < N; j++)
		{
			board[i][j] = 0;
		}
	}

	if(nQueens(board, 0))
	{
		display(board);
	}

	else
	{
		printf("Solution not available\n");
	}

	return 0;
}