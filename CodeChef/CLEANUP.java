import java.util.*;
import java.lang.*;
import java.io.*;


public class Main {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int t = scan.nextInt();

        while (t != 0) {

            int n = scan.nextInt();
            int m = scan.nextInt();

            int[] jobs = new int[n];

            for (int i = 0; i < m; i++) {

                int x = scan.nextInt();
                jobs[x - 1] = 1;

            }

            boolean chef = false;

            for (int i = 0; i < n; i++) {

                if (jobs[i] != 1) {

                    if (!chef) {

                        jobs[i] = 2;
                        chef = true;

                    } else {

                        jobs[i] = 3;
                        chef = false;

                    }

                }

            }

            for (int i = 0; i < n; i++) {

                if (jobs[i] == 2) {
                    System.out.print(i + 1 + " ");
                }

            }

            System.out.println();

            for (int i = 0; i < n; i++) {

                if (jobs[i] == 3) {
                    System.out.print(i + 1 + " ");
                }

            }

            System.out.println();

            t--;

        }

    }

}
