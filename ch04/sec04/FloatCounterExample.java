package ch04.sec04;

public class FloatCounterExample {

	public static void main(String[] args) {
		for(float x = 0.1f; x<=1.0f; x+=0.1f)
			System.out.println(x);
		//카운트에 실수형 변수를 사용하지 말아야 하는 이유.
		//부동소수점 방식은 정확한 0.1을 표현하지 못한다. 
		//따라서 정확한 1.0이 아닌 1.000001 정도의 숫자가 카운트 되어 실제 반복횟수는
		//10번이 아닌 9번이 된다.
	}

}
