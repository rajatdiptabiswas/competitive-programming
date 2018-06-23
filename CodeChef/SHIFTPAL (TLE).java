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

    public static boolean isPalindrome(String str) {

        StringBuilder string = new StringBuilder();
        string.append(str);

        StringBuilder rev = new StringBuilder();
        rev.append(str);
        rev = rev.reverse();

        if (str.contentEquals(rev)) return true;
        else return false;

    }

    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();

            while (t-- > 0) {

                String input = fr.nextLine();
                int length = input.length();
                String check = input + input;

                int count = 0;

                for (int i = 0; i < length; i++) {

                    if (isPalindrome(check.substring(i, length+i))) {
                        count++;
                    }

                }

                System.out.println(count);

            }

        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}