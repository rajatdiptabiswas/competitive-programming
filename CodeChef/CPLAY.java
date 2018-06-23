import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        while(input.hasNext()) {

            String str = input.nextLine();

            int teamA = 0;
            int teamB = 0;
            int teamATurns = 5;
            int teamBTurns = 5;
            int shot;
            int diff;

            boolean ansFound = false;

            for (shot = 0; shot < 10; shot++) {

                if (shot % 2 == 0) {
                    if (str.charAt(shot) == '1') {
                        teamA++;
                        teamATurns--;
                    } else {
                        teamATurns--;
                    }
                } else {
                    if (str.charAt(shot) == '1') {
                        teamB++;
                        teamBTurns--;
                    } else {
                        teamBTurns--;
                    }
                }

                if (teamA > teamB + teamBTurns) {
                    System.out.println("TEAM-A " + (shot+1));
                    ansFound = true;

                    break;
                }

                if (teamB > teamA + teamATurns) {
                    System.out.println("TEAM-B " + (shot+1));
                    ansFound = true;

                    break;
                }
          
            }

            if (ansFound == false) {

                teamA = 0;
                teamB = 0;

                for ( ; shot < str.length(); shot++) {

                    if (shot % 2 == 0) {
                        if (str.charAt(shot) == '1')
                            teamA++;
                    } else {
                        if (str.charAt(shot) == '1')
                            teamB++;

                        diff = Math.abs(teamA - teamB);

                        if (diff > 0) {
                            if (teamA > teamB)
                                System.out.println("TEAM-A " + (shot+1));
                            else
                                System.out.println("TEAM-B " + (shot+1));

                            ansFound = true;

                            break;
                        }
                    }
                }
            }

            if (ansFound == false) {

                System.out.println("TIE");

            }
        }
    }
}
