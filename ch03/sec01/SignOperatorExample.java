package ch03.sec01;

public class SignOperatorExample {

	public static void main(String[] args) {
		int x = -100;
		x = -x;
		System.out.println("x: " + x);
		
		byte b = 100;
		int y = -b;
		System.out.println("y: " + y);
		
		//byte b = 100;
		//byte result = -b;
		//컴파일 에러 발생함. byte에 담긴 값을 연산할 시, int값으로 바뀜. 근데 왜 컴파일에러가 나는 거지? 그냥 다른 값이 담기는 거 아닌가?
	}

}
