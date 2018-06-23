import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


public class Main {

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

    static long sumInBetween(int i, int j, long[] prefix) {

        int l, r;
        if ( i < j ) {
            l = i;
            r = j;
        } else {
            l = j;
            r = i;
        }

        return prefix[r - 1] - prefix[l];
    }

    static int searchLeft(int left, int right, int index, long[] array, long[] prefix) {

        int mid = left + ( (right - left)/2 );

        if ( right == left )
            return right;

        if ( right == left + 1 ) {

            if ( sumInBetween(right, index, prefix) <= array[index] ) {

                if (sumInBetween(left, index, prefix) <= array[index]) {
                    return left;
                } else {
                    return right;
                }

            }
        }

        if ( sumInBetween(index, mid, prefix) <= array[index] ) {
            return searchLeft(left, mid, index, array, prefix);
        } else {
            return searchLeft(mid+1, right, index, array, prefix);
        }

    }

    static int searchRight(int left, int right, int index, long[] array, long[] prefix) {

        int mid = left + ( (right - left)/2 );

        if ( left == right )
            return left;

        if ( left == right - 1 ) {

            if ( sumInBetween(index, left, prefix) <= array[index] ) {

                if ( sumInBetween(index, right, prefix) <= array[index] ) {
                    return right;
                } else {
                    return left;
                }

            }
        }

        if ( sumInBetween(index, mid, prefix) <= array[index] ) {
            return searchRight(mid, right, index, array, prefix);
        } else {
            return searchRight(left, mid-1, index, array, prefix);
        }

    }

    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            long t = fr.nextInt();

            while (t-- > 0) {

                int n = fr.nextInt();
                long[] power = new long[n];
                long[] powerPrefix = new long[n];

                long sum = 0;
                for (int i = 0; i < n; i++) {
                    power[i] = fr.nextLong();
                    sum += power[i];
                    powerPrefix[i] = sum;
                }

                long[] ans = new long[n];
                int l, r;

                for (int i = 0; i < n; i++) {

                    if ( i - 1 >= 0 ) {
                        l = searchLeft(0, i-1, i, power, powerPrefix);
                    } else {
                        l = -1;
                    }

                    if ( i + 1 < n ) {
                        r = searchRight(i+1, n-1, i, power, powerPrefix);
                    } else {
                        r = -1;
                    }

                    if ( l != -1 ) {

                        for (int x = l; x <= i-1; x++) {
                            ans[x] += 1;
                        }

                    }

                    if ( r != -1 ) {

                        for (int x = i+1; x <= r; x++) {
                            ans[x] += 1;
                        }

                    }

                }

                for ( long val : ans ) {
                    System.out.print(val + " ");
                }

                System.out.println();

            }

        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}