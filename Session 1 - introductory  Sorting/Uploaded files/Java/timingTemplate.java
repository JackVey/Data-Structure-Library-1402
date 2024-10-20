class timingTemplate{
	public static void main(String args[]) {
		
		long startTime = System.currentTimeMillis();
		// long startTime = System.nanoTime();
		int s = 0;
		for(int i=1;i<=1000000000;i++)
			s+=i;
		System.out.println("Sum = "+s);
		long endTime = System.currentTimeMillis();
		// long stopTime = System.nanoTime();		
		System.out.println("Elapsed time: " + (endTime - startTime) + " milliseconds");
	}
}

