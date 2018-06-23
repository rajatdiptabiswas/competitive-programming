import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


public class Main {

	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) {
		
		int t;

		try {
			
			t = Integer.parseInt(br.readLine().trim());
			
			while (t-- > 0) {	

				StringTokenizer st = new StringTokenizer(br.readLine());
			    int n = Integer.parseInt(st.nextToken());
			    int x = Integer.parseInt(st.nextToken());

			    int[] notes = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

			    int sum = 0;
			    Integer min = Integer.MAX_VALUE;

			    for (int i = 0; i < notes.length; i++)
			    {
			    	sum += notes[i];

			    	if (notes[i] < min) {
			    		min = notes[i];
			    	}
			    }

			    if (sum % x >= min) {
			    	System.out.println("-1");
			    } else {
			    	System.out.println(sum/x);
			    }

			}

		} catch (IOException e) {

			e.printStackTrace();
		}
		
	}

}