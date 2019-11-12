import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


class PHCUL {

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

    static class Point {

        Double x;
        Double y;
    
        Point(Double x, Double y) {
            this.x = x;
            this.y = y;
        }
    
        Double distance(Point p) {
            return Math.sqrt(Math.pow((p.x - this.x), 2) + Math.pow((p.y - this.y), 2));
        }
    
    }

    public static void main(String[] args) {

        try {

            FastReader fr = new FastReader();

            int t = fr.nextInt();

            while (t-- > 0) {

                Double x = fr.nextDouble();
                Double y = fr.nextDouble();

                Point sc = new Point(x,y);

                Long n = fr.nextLong();
                Long m = fr.nextLong();
                Long k = fr.nextLong();

                ArrayList<Point> nArray = new ArrayList<>();
                ArrayList<Point> mArray = new ArrayList<>();
                ArrayList<Point> kArray = new ArrayList<>();

                for (int i = 0; i < n; i++) {
                    nArray.add(new Point(fr.nextDouble(), fr.nextDouble()));
                }

                for (int i = 0; i < m; i++) {
                    mArray.add(new Point(fr.nextDouble(), fr.nextDouble()));
                }

                for (int i = 0; i < k; i++) {
                    kArray.add(new Point(fr.nextDouble(), fr.nextDouble()));
                }

                // sc -> n -> m -> k
                Double distanceNM = Double.MAX_VALUE;
                Double tempDistanceNM;
                
                for (int p = 0; p < n; p++) {
                    
                    tempDistanceNM = sc.distance(nArray.get(p));
                    
                    if (distanceNM < tempDistanceNM) 
                        continue;
                    
                    for (int q = 0; q < m; q++) {
                        
                        tempDistanceNM = sc.distance(nArray.get(p));
                        tempDistanceNM += nArray.get(p).distance(mArray.get(q));
                        
                        if (distanceNM < tempDistanceNM) 
                            continue;

                        for (int r = 0; r < k; r++) {
                            
                            tempDistanceNM = sc.distance(nArray.get(p)) + nArray.get(p).distance(mArray.get(q));
                            tempDistanceNM += mArray.get(q).distance(kArray.get(r));

                            distanceNM = Math.min(distanceNM, tempDistanceNM);

                        }
                    }
                }

                // sc -> m -> n -> k
                Double distanceMN = Double.MAX_VALUE;
                Double tempDistanceMN;
                
                for (int p = 0; p < m; p++) {
                    
                    tempDistanceMN = sc.distance(mArray.get(p));
                    
                    if (distanceMN < tempDistanceMN) 
                        continue;
                    
                    for (int q = 0; q < n; q++) {
                        
                        tempDistanceMN = sc.distance(mArray.get(p));
                        tempDistanceMN += mArray.get(p).distance(nArray.get(q));
                        
                        if (distanceMN < tempDistanceMN) 
                            continue;

                        for (int r = 0; r < k; r++) {
                            
                            tempDistanceMN = sc.distance(mArray.get(p)) + mArray.get(p).distance(nArray.get(q));
                            tempDistanceMN += nArray.get(q).distance(kArray.get(r));

                            distanceMN = Math.min(distanceMN, tempDistanceMN);

                        }
                    }
                }

                Double minDistance = Math.min(distanceNM, distanceMN);

                System.out.println(minDistance);

            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}