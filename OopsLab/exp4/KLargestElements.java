package OopsLab.exp4;

/**
 * Write a Java program to find the k largest elements in a given array. 
 * Elements in the array can be in any order.
 */

import java.util.Scanner;

import java.util.Arrays;

public class KLargestElements {

    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {

            System.out.print("Enter array size: ");

        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter array elements:");

        for (int i = 0; i < n; i++) {

            arr[i] = sc.nextInt();

        }

        System.out.print("Enter value of k: ");

        int k = sc.nextInt();

        Arrays.sort(arr);

        System.out.println("K largest elements:");

        for (int i = n - 1; i >= n - k; i--) {

            System.out.print(arr[i] + " ");

        }

    }

}