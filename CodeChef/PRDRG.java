import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


class Main {

    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            
            while (st == null || !st.hasMoreElements()) { 
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException  e) {
                    e.printStackTrace();
                }
            }

            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {      	
            
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }

            return str;
        }
    }

    static int findDenominator(int n) {

        return (int)Math.pow(2, n);

    }

    static int findNumerator(int n) {

        if (n == 1 || n == 2) return 1;

        int right = findDenominator(n) - 1;
        int left = 0;
        int mid = 0;

        int count = 0;

        while (right - left > 1) {

            mid = (left + right) / 2;

            if (count % 2 == 0) {
                right = mid;
            } else {
                left = mid;
            }

            count++;

        }

        return mid + 1;

    }


    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();

            while (t-- > 0) {

            	int n = fr.nextInt();
                
                System.out.println(findNumerator(n) + " " + findDenominator(n));

            }

            System.out.println();


        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}