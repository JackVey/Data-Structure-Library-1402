package DS;

import java.util.Random;

public class randGenTemplate {
    public static int[] randArray(int seed, int n)
    {
        Random rd = new Random(seed); // creating Random object
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++)
        {
            arr[i] = rd.nextInt();
        }
        return arr;
    }

    public static void main(String[] args)
    {
        int n=1000000;
        int[] arr = randArray(1401, n);
        SaveArrayToFile.saveArray(arr, "arr_1000.txt");
    }
}