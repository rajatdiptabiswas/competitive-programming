import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


class SQRDSUB {

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


    static boolean isGood(int num) {
        if (num % 4 == 2) {
            return false;
        } else {
            return true;
        }
    }


    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();

            while (t-- > 0) {

                int n = fr.nextInt();
                int input = 0;
                ArrayList<Integer> arr = new ArrayList<>();
                for (int x = 0; x < n; x++) {
                    input = fr.nextInt() % 4;
                    if (input < 0) {
                        input += 4;
                    }
                    arr.add(input);
                }

                boolean allOdd = true;

                for (int a : arr) {
                    if (a % 2 == 0) {
                        allOdd = false;
                    }
                }

                int count;

                if (n % 2 == 0) {
                    count = ((n/2) * (n+1));
                } else {
                    count = (((n+1)/2) * n);
                }

                if (!allOdd) {
                    int val = 0;
                    int zeroCount = 0;
                    int twoCount = 0;

                    for (int i = 0; i < n; i++) {
                        zeroCount = 0;
                        val = arr.get(i) % 4;
                        if (!isGood(val)) {
                            twoCount += 1;
                        }
                        // System.out.println(i + " " + 0);
                        // System.out.println(twoCount);
                        for (int j = i+1; j < n; j++) {
                            val *= arr.get(j);
                            val %= 4;
                            if (!isGood(val)) {
                                twoCount += 1;
                            }
                            // System.out.println(i + " " + j);
                            // System.out.println(twoCount);
                        }
                        if (zeroCount == n-i) {
                            break;
                        }
                    }

                    count -= twoCount;
                }

                System.out.println(count);

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}