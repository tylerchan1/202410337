package ch03.sec03;

public class OverflowUnderflowExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte var1 = 125;
		for(int i = 0; i < 5; i++) {
			var1++; //이것도int로 자동형변환? - 형변환 안되네.
			//0111 1101 125
			//0111 1110 126
			//0111 1111 127
			//1000 0000 -128
			//1000 0001? -127
			//1000 0010 -126
			System.out.println("var1: " + var1);
		}

		System.out.println("----------------------");
		
		byte var2 = -125;
		for (int i = 0; i < 5; i++) {
			var2--;
			//1000 0011 -125
			//1000 0010 -126
			//1000 0001 -127
			//1000 0000 -128
			//0111 1111 127
			System.out.println("var2: " + var2);
		}
	}

}



