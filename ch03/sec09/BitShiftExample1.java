package ch03.sec09;

public class BitShiftExample1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num1 = 1;
		int result1 = num1 << 3;
		int result2 = num1 * (int) Math.pow(2, 3);
		System.out.println("result1: " + result1);
		System.out.println("result2: " + result2);
		// 0000 0001 > 0000 0010 > 0000 0100 > 0000 1000
		int num2 = -8;
		// 1111 1111 1000 > 1111 1100 > 1111 1110 > 1111 1111
		// 111~ 111 = 모든 숫자가 1로 채워진 값의 2의보수는 00000001 = 1임(-1)
		int result3 = num2 >> 3;
		int result4 = num2 / (int) Math.pow(2, 3);
		System.out.println("result3: " + result3);
		System.out.println("result4: " + result4);
		

	}

}
