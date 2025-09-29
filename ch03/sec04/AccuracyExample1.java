package ch03.sec04;

public class AccuracyExample1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//int apple = 1;
		int apple = 10; //사과 1개를 10조각으로 생각
		//double pieceUnit = 0.1;
		int pieceUnit = 1;
		int number = 7;
		
		//double result = apple - number * pieceUnit; //double로 하면 3.0이 출력됨
		int result = apple - number * pieceUnit;
		double r = result/10.0; // 나누기10과 나누기 10.0은 그 결과가 다르다.; 0,0.3;
		System.out.println("사과 10조각에서 남은 조각: " + result);
		System.out.println("사과 1개에서 남은 양: " + r);
	}

}
