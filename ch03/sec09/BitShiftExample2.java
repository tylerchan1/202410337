package ch03.sec09;

public class BitShiftExample2 {
	public static void main(String[] args) {
		int value = 772; //0~0 0~0  0~0 0~0  0~0 0011 0~0 0100
		
		//우측으로 3바이트 이동, 끝 1바이트 읽기
		byte byte1 = (byte)(value >>> 24);//괄호 무조건 해줘야되네;
		int int1 = byte1 & 255;
		System.out.println("첫 번째 바이트 부호 없는 값:" + int1);
		//우측으로 2바이트 이동, 끝 1바이트 읽기
		byte byte2 = (byte)(value >>> 16);//괄호 무조건 해줘야되네;
		int int2 = byte2 & 255;
		System.out.println("첫 번째 바이트 부호 없는 값:" + int2);
		//우측으로 1바이트 이동, 끝 1바이트 읽기
		byte byte3 = (byte)(value >>> 8);//괄호 무조건 해줘야되네;
		int int3 = byte3 & 255;
		System.out.println("첫 번째 바이트 부호 없는 값:" + int3);
		// 끝 1바이트 읽기
		byte byte4 = (byte)value;//괄호 무조건 해줘야되네;
		int int4 = byte4 & 255;
		System.out.println("첫 번째 바이트 부호 없는 값:" + int4);
		
		
		
	}
}
