import java.util.*;
import java.lang.*;
import java.io.*;


class BITOBYT {

	static Scanner scan = new Scanner(System.in);

	public static void main(String[] args) {
		
		int t = scan.nextInt();

		while (t-- > 0) {

			long n = scan.nextInt();
			n--;

			long population = (long)Math.pow(2.0,n/26);
			long remaining = n % 26;

			if (remaining >= 0 && remaining < 2) {
				System.out.println(population + " 0 0");
			} else if (remaining >= 2 && remaining < 10) {
				System.out.println("0 " + population + " 0");
			} else if (remaining >= 10 && remaining < 26) {
				System.out.println("0 0 " + population);
			}

		}

	}

}