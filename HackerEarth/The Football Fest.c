#include <stdio.h>

void push(int stack[], int val, int *top)
{
	*top = *top+1;
	stack[*top] = val;
}

void pop(int stack[], int *top)
{
	*top = *top-1;
}

int main()
{
	int t;
	char curr, prev;
	scanf("%d", &t);

	while(t--)
	{
		int n, initid, id;
		scanf("%d %d", &n, &initid);

		int stack[n];
		int top = -1;

		stack[++top] = initid;
		
		for(int i = 0; i < n; i++)
		{
			
			scanf(" %c", &curr);

			if(curr == 'P')
			{
				scanf("%d", &id);
				push(stack, id, &top);

				prev = 'P';
			}

			else if(curr == 'B')
			{
				if(curr == prev)
				{
					top++;
					prev = 'P';
				}
				
				else
				{
					pop(stack, &top);
					prev = 'B';
				}

			}
		}

		printf("Player %d\n", stack[top]);
	}

	return 0;
}