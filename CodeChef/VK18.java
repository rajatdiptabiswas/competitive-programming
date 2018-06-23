import java.util.*;
import java.lang.*;
import java.io.*;


public class Main {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int t = scan.nextInt();

        long prefixRooms[] = new long[2*1000001];
        long diamondAns[] = new long[1000001];

        for (int x = 1; x < 2*1000001; x++) {
            prefixRooms[x] = prefixRooms[x-1] + diamond(x);
        }

        for (int y = 1; y < 1000001; y++) {
            diamondAns[y] = diamondAns[y-1] + (2 * (prefixRooms[(2*y)-1] - prefixRooms[y])) + diamond(2*y);
        }

        while (t != 0) {

            int q = scan.nextInt();

            System.out.println(diamondAns[q]);

            t--;
        }
    }


    private static long diamond(long room) {

        long even = 0;
        long odd = 0;
        long val;

        while (room > 0) {

            val = room % 10;

            if ((val % 2) == 0) {
                even += val;
            } else {
                odd += val;
            }

            room /= 10;
        }

        return Math.abs(even - odd);
    }

}