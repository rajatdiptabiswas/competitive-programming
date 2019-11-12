import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


class Pair {

    int value;
    int color;

    Pair(int value, int color) {
        this.value = value;
        this.color = color;
    }

    int getValue() {
        return this.value;
    }

    int getColor() {
        return this.color;
    }

}


class CAMC {

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
                Integer m = fr.nextInt();

                ArrayList<Pair> array = new ArrayList<>();

                for (int x = 0; x < n; x++) {
                    Integer input = fr.nextInt();
                    array.add(new Pair(input, x%m));
                }

                Collections.sort(array, new Comparator<Pair>() {
                    @Override
                    public int compare(Pair p1, Pair p2) {
                        // if (p1.getValue() == p2.getValue()) {
                        //     return p1.getColor() - p2.getColor();
                        // }
                        return p1.getValue() - p2.getValue();
                    }
                });

                // for (Pair p : array) {
                //     System.out.println(p.getValue() + "\t-> " + p.getColor());
                // }


                // 4 8 2 6 12 14 10 16 18
                // 0 1 2 0 1  2  0  1  2

                // 0  1  2  3  4  5  6  7  8
                // 2  4  6  8 10 12 14 16 18
                // 2  0  0  1  0  1  2  1  2

                Integer l = 0;
                Integer r = 0;

                ArrayList<Integer> ans = new ArrayList<>();

                HashMap<Integer, Integer> colorFreq = new HashMap<>();

                Integer key;

                while (r < n) {

                    key = array.get(r).getColor();
                    if (colorFreq.containsKey(key)) {
                        colorFreq.put(key, colorFreq.get(key) + 1);
                    } else {
                        colorFreq.put(key, 1);
                    }

                    while (colorFreq.size() == m) {

                        ans.add(array.get(r).getValue() - array.get(l).getValue());
                        
                        key = array.get(l).getColor();
                        colorFreq.put(key, colorFreq.get(key) - 1);

                        if (colorFreq.get(key) == 0) {
                            colorFreq.remove(key);
                        }
                        
                        l++;

                    }

                    r++;

                }

                // for (int x : ans) {
                //     System.out.print(x + " ");
                // }
                // System.out.println();

                System.out.println(Collections.min(ans));

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}