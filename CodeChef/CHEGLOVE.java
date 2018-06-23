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

            Long t = fr.nextLong();

            while (t-- > 0) {

                int n = fr.nextInt();

                ArrayList<Long> fingers = new ArrayList<>();

                for (int i = 0; i < n; i++) {

                    fingers.add(fr.nextLong());

                }

                ArrayList<Long> gloves = new ArrayList<>();

                for (int i = 0; i < n; i++) {

                    gloves.add(fr.nextLong());

                }

                ArrayList<Long> glovesReversed = (ArrayList<Long>) gloves.clone();

                Collections.reverse(glovesReversed);

                boolean willFit = true;
                boolean willFitReversed = true;

                for (int i = 0; i < n; i++) {

                    if ( fingers.get(i) > gloves.get(i) && willFit) {

                        willFit = false;

                    }

                    if ( fingers.get(i) > glovesReversed.get(i) && willFitReversed) {

                        willFitReversed = false;

                    }

                }

                if ( willFit && willFitReversed ) {

                    System.out.println("both");

                } else if ( willFit ){

                    System.out.println("front");

                } else if ( willFitReversed ) {

                    System.out.println("back");

                } else {

                    System.out.println("none");

                }

            }

        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}