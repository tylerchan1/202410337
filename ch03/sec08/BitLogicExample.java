package ch03.sec08;

public class BitLogicExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("45 & 25 = " + (45 & 25));
		//45: 0010 1101, 25: 0001 1001 
		//&비트연산시 0000 1001 = 9
		System.out.println("45 | 25 = " + (45 | 25));
		//|비트연산시 0011 1101 = 61
		System.out.println("45 ^ 25 = " + (45 ^ 25));
		//^비트연산시 0011 0100 = 52
		System.out.println("~45 = " + (~45));
		//~연산시 0010 1101에서 1101 0010 -46
		//엥? 어떻게 -46이 나오지?
		System.out.println("---------------------------------");
		
		byte receiveData = -120; //120: 0111 1000/ 1의 보수 1000 0111
		
		//방법1: 비트 논리곱 연산으로 Unsigned 정수 얻기
		int unsignedInt1 = receiveData & 255;//(byte타입) & (int타입) ->int타입으로 형변환
		//원래숫자-120 = 0111 1000
		//1의 보수 135 = 1000 0111
		//2의 보수 136 = 1000 1000
		//255: 1111 1111임? int로 하면 되는데 byte로 하면 안됨
		//& 255 연산의 역할: 255는 16진수로 0xFF이며, 2진수로 11111111입니다. 
		//32비트 int로 표현하면 00000000 00000000 00000000 11111111이 됩니다. 
		//이 값과 비트 논리곱을 하면, 확장된 상위 비트(24비트)는 모두 0이 되고, 원래 8비트 값만 남게 됩니다.
		System.out.println(unsignedInt1);
		System.out.println(receiveData);
		
		int unsignedInt2 = Byte.toUnsignedInt(receiveData);
		System.out.println(unsignedInt2);
		
		int test = 136;// 00000~0000 1000 1000 -> 1000 1000 => 0111 1000(-120)
		byte btest = (byte) test; //-120
		System.out.println(btest);
	}
}
