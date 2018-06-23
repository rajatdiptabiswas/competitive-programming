import java.util.*;
import java.io.*;
import java.lang.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Main {

    public static Scanner scan = new Scanner(System.in);

    public static void main(String[] args) {

        int t = scan.nextInt();

        while (t-- > 0) {

            String str = scan.next();

            Integer strlen = str.length();

            String ans = new String();

            for (int i = strlen-1; i >= 0; i--) {

                ans += str.charAt(i);

            }

            System.out.println(Integer.parseInt(ans));
        }

    }

}
