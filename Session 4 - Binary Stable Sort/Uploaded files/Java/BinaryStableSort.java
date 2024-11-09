import java.util.Random;

public class BinaryStableSort {
    public static void blockSwap(aclass[] arr, int p, int q){
        // TO DO
    }

    public static int stableSRBA(aclass[] arr, int p, int q, int r){
        int n0 = r - q;
        int n1 = q - p;
        if (n1==0) return r;
        while (n0 > 0){
            if (n1 > n0){
                p = q - n0;
                blockSwap(arr, p, q);
                n1 = n1 - n0;
                q = p;
                p = p - n1;
            }else {
                blockSwap(arr, p, q);
                n0 = n0 - n1;
                p = q;
                q = q + n1;
            }
        }
        return p;
    }

    public static int binaryStableSort(aclass[] arr, int p, int r) {
        if (r - p > 1) {
            int q = (p + r) / 2;
            p = binaryStableSort(arr, p, q);
            r = binaryStableSort(arr, q, r);
            p = stableSRBA(arr, p, q, r);
        } else {
            if (arr[p].k == 0) {
                 //return ?;
            }
        }
        return p;
    }


    public static class aclass{
        int k;
        char satellite;

        public void setK(int k) {
            this.k = k;
        }

        public void setSatellite(char satellite) {
            this.satellite = satellite;
        }


        void print(){
            System.out.println("(" + this.k + ", " + this.satellite + ")");
        }

    }
    public static void main(String[] args) {
        Random random = new Random();
        aclass A[] = new aclass[26];
        for(int i=0;i<26;i++) {
            int rand = random.nextInt(2) ;
            aclass ac = new aclass();
            ac.setK(rand);
            int index = i + 97;
            char data = (char) index;
            ac.setSatellite(data);

            A[i]= ac;
        }
        for(int i=0;i<26;i++) A[i].print();
        System.out.println();
        binaryStableSort(A,0,26);
        for(int i=0;i<26;i++) A[i].print();
        System.out.println();

    }


}
