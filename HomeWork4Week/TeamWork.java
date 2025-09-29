package HomeWork4Week;
import java.util.Scanner;

public class TeamWork {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean run = true;
		int n;
		int total=0 ,minus=0, plus = 0;
		while (run) {
			System.out.println("----------------------------");
			System.out.println("1.예금 | 2.출금 | 3.잔고 | 4.종료");
			System.out.println("----------------------------");
			System.out.print("선택> ");
			n = sc.nextInt();
			switch(n) {
			case 1:
				System.out.print("예금액>");
				plus = sc.nextInt();
				total += plus;
				System.out.println("잔고>" + total);
				System.out.print("\n");
				break;
			case 2:
				System.out.print("출금액>");
				minus = sc.nextInt();
				total -= minus;
				System.out.println("잔고>" + total);
				System.out.print("\n");
				break;
			case 3:
				System.out.println("잔고>" + total);
				System.out.print("\n");
				break;
			case 4:
				System.out.print("\n프로그램 종료");
				run = false;
			}
		}
	}

}
