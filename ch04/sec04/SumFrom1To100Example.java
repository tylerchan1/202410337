package ch04.sec04;

public class SumFrom1To100Example {

	public static void main(String[] args) {
		int sum = 0;
		int i;//밖에서 i를 선언해야하는 이유, for문 밖에서도 i가 쓰여서
		
		for(i = 1; i<=100; i++) 
			sum += i;
		
		System.out.println("1~" + (i-1) + " 합: " + sum);
	}

}
