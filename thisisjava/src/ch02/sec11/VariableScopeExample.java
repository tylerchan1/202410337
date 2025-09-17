package ch02.sec11;

public class VariableScopeExample {
	public static void main(String[] args) {
		int v1 = 15;
		int v2 = 0;
		if(v1>10) {
			v2 = v1 - 10;
		}
		int v3 = v1 + v2 + 5; //v2변수를 if블록 안에서 선언하면 외부에서 사용할 수 없기 때문에 컴파일 에러가 생긴다. 주의.
		//System.out.println(v3);
	}

}
