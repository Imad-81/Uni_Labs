package OopsLab.exp4;

/**
 * 4.1. Write a Java program to create a two-dimensional array (m x m) A[][] such that A[i][j] is false if I and j are prime, otherwise A[i][j] becomes true.
 */

import java.util.Scanner;

public class PrimeIndexArray {

    public static boolean isPrime(int n) {

        if (n < 2)
            return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {

            if (n % i == 0)

                return false;

        }

        return true;

    }

    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {

            System.out.print("Enter value of m: ");

        int m = sc.nextInt();

        boolean[][] A = new boolean[m][m];

        for (int i = 0; i < m; i++) {

            for (int j = 0; j < m; j++) {

                if (isPrime(i) && isPrime(j)) {

                    A[i][j] = false;

                } else {

                    A[i][j] = true;

                }

            }

        }

        for (int i = 0; i < m; i++) {

            for (int j = 0; j < m; j++) {

                System.out.print(A[i][j] + " ");

            }

            System.out.println();

        }

    }

}
