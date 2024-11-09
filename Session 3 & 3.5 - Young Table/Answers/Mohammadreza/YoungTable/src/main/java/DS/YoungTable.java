package DS;

public class YoungTable {
    int[] A;
    private final int size;
    private final int row;
    private final int column;
    YoungTable(int[] A, int row, int column){
        this.A = A.clone();
        this.row = row;
        this.column = column;
        this.size = row * column;

    }

    public int getAt(int i, int j){
        return A[i * column + j];
    }

    public void indexToRowCol(int index) {
        int j = index % column;
        int i = index / row;
        System.out.println("i: " + (i - 1));
        System.out.println("j: " + (j - 1));
    }

    public Integer rowColToIndex(int i, int j) {
        if (i * this.column + j >= this.size) {
            return null;
        }
        return i * this.column + j + 1;
    }


    public void setAt(int i, int j, int x){
        A[i * column + j] = x;
    }

    private void siftDown(int i, int j){
        int currentNum = getAt(i, j);

        boolean existDown = i < this.row - 1;
        boolean existRight = j < this.column - 1;

        int downNeighbor = existDown ? this.getAt(i + 1, j) : Integer.MIN_VALUE;
        int rightNeighbor = existRight ? this.getAt(i, j + 1) : Integer.MIN_VALUE;

        if (!existDown && !existRight) {
            return;
        }

        int maxNeighbor;
        if (existDown && existRight) {
            maxNeighbor = Math.max(downNeighbor, rightNeighbor);
        } else if (existRight) {
            maxNeighbor = rightNeighbor;
        } else {
            maxNeighbor = downNeighbor;
        }

        if (currentNum < maxNeighbor) {
            if (existRight && existDown && maxNeighbor == rightNeighbor) {
                this.setAt(i, j, maxNeighbor);
                this.setAt(i, j + 1, currentNum);
                this.siftDown(i, j + 1);
            } else if (existRight && existDown) {
                this.setAt(i, j, maxNeighbor);
                this.setAt(i + 1, j, currentNum);
                this.siftDown(i + 1, j);
            } else if (existRight) {
                this.setAt(i, j, maxNeighbor);
                this.setAt(i, j + 1, currentNum);
                this.siftDown(i, j + 1);
            } else {
                this.setAt(i, j, maxNeighbor);
                this.setAt(i + 1, j, currentNum);
                this.siftDown(i + 1, j);
            }
        }


    }

    public void buildYoungTable() {
        for (int i = row - 1; i >= 0; i--) {
            for (int j = column - 1; j >= 0; j--) {
                this.siftDown(i, j);
            }
        }
    }

    public void printTable() {
        System.out.println("\nTable:\n");
        for (int i = 0; i < A.length; i++) {
            if (i % column == 0 && i != 0) {
                System.out.println();
            }
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }

    public boolean test(){
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column - 1; j++) {
                if (getAt(i, j) < getAt(i, j + 1))
                    return false;
            }
        }

        for (int i = 0; i < column; i++) {
            for (int j = 0; j < row - 1; j++) {
                if (getAt(j, i) < getAt(j + 1, i))
                    return false;
            }
        }

        return true;
    }

    public static void benchmark(){
        int[] A = LoadArrayFromFile.loadArray("arr_1000.txt");
        YoungTable matrix = new YoungTable(A, 1000, 1000);
        long startTime = System.currentTimeMillis();
        matrix.buildYoungTable();
        long endTime = System.currentTimeMillis();
        System.out.println("Elapsed time: " + (endTime - startTime) + " milliseconds");
    }

    public static void main(String[] args) {
        benchmark();
//        int[] A = { 97, 11, 40, 81, 45, 58, 55, 60, 67, 62, 57, 95, 64, 36, 30, 1, 72, 96, 66, 13, 18, 28, 93, 68 };
//        YoungTable matrix = new YoungTable(A, 4, 6);
//
//        matrix.printTable();
//        matrix.buildYoungTable();
//        System.out.println(matrix.test());
//        matrix.printTable();
//
//        System.out.println(matrix.getAt(0, 0));
//        System.out.println(matrix.rowColToIndex(1,2));
//        matrix.indexToRowCol(matrix.rowColToIndex(1,2));
//
//        matrix.setAt(2, 2, 15);
//        matrix.printTable();
//        matrix.buildYoungTable();
//        matrix.printTable();
//        System.out.println(matrix.test());
    }
}
