import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


class HMAPPY2 {

    static long GCD(long a, long b) {
        if (b == 0)
            return a;
        
        return GCD(b, a%b);
    }

    static long LCM(long a, long b) {
        return (a*b) / GCD(a,b);
    }

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


    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();

            while (t-- > 0) {

                long n = fr.nextLong();
                long a = fr.nextLong();
                long b = fr.nextLong();
                long k = fr.nextLong();

                long lcm = LCM(a,b);
                long count = 0;

                // for (int x = 0; x < n; x++) {

                //     if ((x % a == 0 && x % b != 0 && x % lcm != 0) || (x % b == 0 && x % a != 0 && x % lcm != 0))
                //         count++;

                // }

                count += (n/a) - (n/lcm);
                count += (n/b) - (n/lcm);

                if (count >= k)
                    System.out.println("Win");
                else
                    System.out.println("Lose");

                // System.out.println(lcm);

            }

        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}