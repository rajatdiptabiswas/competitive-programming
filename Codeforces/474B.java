import java.util.*;
import java.lang.*;
import java.io.*;

public class Worms {

	static int solve(int l, int r, int key, int[] array) {

		int ans = -1;

		int mid;
		int found;

		while (l <= r) {

			mid = l + (int)((r-l)/2);
			found = array[mid];
	
			if (found < key) {
				ans = mid;
				l = mid+1;
			} else if (found >= key) {
				r = mid-1;
			}
			
		}

		return ans+1;

	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] arr = new int[n];
		int[] prefix = new int[n+1];

		for (int x = 0; x < n; x++) {
			arr[x] = sc.nextInt();
		}
		
		prefix[0] = 0;
		for (int y = 0; y < n; y++) {
			prefix[y+1] = prefix[y] + arr[y];
		}

		// System.out.println(Arrays.toString(prefix));
		
		int x = sc.nextInt();
		while (x-- > 0) {
			
			int key = sc.nextInt();
			System.out.println(solve(0, prefix.length, key, prefix));

		}

	}

}
