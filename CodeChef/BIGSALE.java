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


    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();
            int price, quantity, discount, n;
            double loss;

            while (t-- > 0) {

                n = fr.nextInt();

                loss = 0;

                for (int i = 0; i < n; i++) {

                    price = fr.nextInt();
                    quantity = fr.nextInt();
                    discount = fr.nextInt();

                    loss += (price * quantity) - (price * quantity * (100 + discount) * 0.01 * (100 - discount) * 0.01);

                }

                System.out.println(loss);

            }

        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}