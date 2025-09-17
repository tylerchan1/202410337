package ch02.sec07;

public class PromotionExample {
	public static void main(String[] args) {
		//자동 타입 변환
		byte byteValue = 10;
		int intValue = byteValue;
		System.out.println("intValue: " + intValue);
		
		char charValue = '가';
		intValue = charValue;
		System.out.println("가의 유니코드: " + intValue);
		
		intValue = 50;
		long longValue = intValue;
		System.out.println("longValue: " + longValue);
		
		longValue = 100;
		float floatValue = longValue;
		System.out.println("floatVlaue: " + floatValue);//왜 출력이 소수점 한 자리 숫자까지 밖에 안되는가?
		
		floatValue = 100.5F;//뭐지 100.5F double로 바뀌지 않게 f 마지막에 넣어둔 것임.
		double doubleValue = floatValue;
		System.out.println("doubleValue: " + doubleValue);
	}
}
