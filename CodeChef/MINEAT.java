import java.util.*;
import java.io.*;
import java.lang.*;


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

    static int timeTaken(ArrayList<Integer> arr, int k) {

        int time = 0;

        for ( int i : arr ) {

            if ( i <= k ) {

                time++;

            } else {

                if ( i % k == 0 ) {

                    time += i/k;

                } else {

                    time += i/k + 1;

                }
            }

        }

        return time;

    }

    static int searchK(int left, int right, ArrayList<Integer> arr, int hrs) {

        int mid = left + (right - left)/2;
        int time = timeTaken(arr, mid);

        if ( left == right ) {
            return mid;
        }

        if ( time <= hrs ) {
            return searchK(left, mid, arr, hrs);
        } else  {
            return searchK(mid+1, right, arr, hrs);
        }

    }

    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();

            while (t-- > 0) {

                int n = fr.nextInt();
                int hrs = fr.nextInt();

                ArrayList<Integer> banana = new ArrayList<>();

                for (int i = 0; i < n; i++) {
                    banana.add(fr.nextInt());
                }

                Collections.sort(banana);

                int l = 1;
                int r = banana.get(banana.size() - 1);

                System.out.println(searchK(l, r, banana, hrs));

            }

        } catch (Exception e) {

            e.printStackTrace();
        }

    }

}