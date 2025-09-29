package ch04.sec08;

public class ContinueExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i = 1; i<=10; i++) {
			if (i%2 != 0)//i가 2로 나눠지지 않으면 continue(밑에 코드 실행하지 않고 다음 반복으로 넘어감)
				continue;
			System.out.println(i + " ");
		}

	}

}
