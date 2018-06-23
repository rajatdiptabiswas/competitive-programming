import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;


public class Main {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) {

        try {

            int t = Integer.parseInt(br.readLine().trim());

            String[] chef = {"chef", "chfe", "cehf", "cefh", "cfhe", "cfeh", "hcef", "hcfe", "hecf", "hefc", "hfce", "hfec", "echf", "ecfh", "ehcf", "ehfc", "efch", "efhc", "fche", "fceh", "fhce", "fhec", "fech", "fehc"};

            while (t-- > 0) {

                String str = br.readLine().trim();
                int count = 0;
                boolean flag = false;

                for (int i = 4; i <= str.length(); i++) {

                    if (Arrays.asList(chef).contains(str.substring(i-4,i))) {

                        flag = true;
                        count += 1;

                    }

                }

                if (flag) {

                    System.out.println("lovely " + count);

                } else {

                    System.out.println("normal");

                }

            }

        } catch (IOException e) {

            e.printStackTrace();
        }

    }

}
