package DS;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class SaveArrayToFile {

    public static void saveArray(int[] array, String filename) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filename))) {
            for (int i = 0; i < array.length; i++) {
                writer.write(array[i] + " ");
            }
            writer.newLine();
        } catch (IOException e) {
            System.out.println("An error occurred while saving the array: " + e.getMessage());
        }
    }
}
