package DS;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class LoadArrayFromFile {

    public static int[] loadArray(String filename) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line = reader.readLine();
            if (line != null) {
                String[] numbers = line.split(" ");
                for (String num : numbers) {
                    arrayList.add(Integer.parseInt(num));
                }
            }
        } catch (IOException e) {
            System.out.println("An error occurred while reading the array: " + e.getMessage());
        }

        // تبدیل ArrayList به آرایه
        int[] array = new int[arrayList.size()];
        for (int i = 0; i < arrayList.size(); i++) {
            array[i] = arrayList.get(i);
        }
        return array;
    }
}
