import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;

// n strings [s1, s2, ..., sN]
// ingredients chars

class CHEFING {

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

                Integer n = fr.nextInt();

                boolean[] boolArray1 = new boolean[26];
                Arrays.fill(boolArray1, true);

                boolean[] boolArray2 = new boolean[26];
                
                ArrayList<String> input = new ArrayList<>();
                for (int i = 0; i < n; i++) {
                    String str = fr.next();
                    input.add(str);

                    Arrays.fill(boolArray2, false);

                    for (char c : str.toCharArray()) {
                        boolArray2[(int)(c - 'a')] = true;
                    }

                    for (int j = 0; j < 26; j++) {
                        boolArray1[j] = (boolArray1[j] && boolArray2[j]);
                    }
                }
                
                int count = 0;

                for (int x = 0; x < 26; x++) {
                    if (boolArray1[x])
                        count++;
                }

                System.out.println(count);

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}