package ch03.sec02;

public class ArithmeticOperatorExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte v1 = 10;
		byte v2 = 4;
		long v4 = 10L; //float으로 자동형변환 막기
		
		int result1 = v1 + v2; //모든 피연산자는 int타입으로 자동 변환 후 연산
		System.out.println("result1: " + result1);//14
		
		long result2 = v1 + v2 - v4; //모든 피연산자는 long 타입으로 자동 변환 후 연산
		System.out.println("result2: " + result2);//4
		
		double result3 = (double) v1 / v2; //강제 형 변환, 왜 이것만 강제 형변환?
		System.out.println("result3: " + result3);//2.5
		
		int result4 = v1 % v2;
		System.out.println("result4: " + result4);//2
		

	}

}
