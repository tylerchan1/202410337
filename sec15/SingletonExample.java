package ch06.sec15;

public class SingletonExample {
	public static void main(String[] args) {
		//Singleton obj1 = new Singleton(); //컴파일 에러
	
		//정적 메소드를 호출해서 싱글톤 객체 얻기
		Singleton obj2 = Singleton.getInstance();
		Singleton obj3 = Singleton.getInstance();
		
		if(obj2 == obj3) System.out.println("같은 Singleton 객체 입니다.");
		else System.out.println("다른 Singleton 객체 입니다.");
	}
}
