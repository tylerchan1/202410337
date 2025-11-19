package HomeWork4Week.sd;
import java.util.Scanner;

public class BankApplication {
	
    private static Account[] accountArray = new Account[100];
    private static Scanner sc = new Scanner(System.in);
    private static boolean run = true;


    public static void main(String[] args) {

        while (run) {
            System.out.println("------------------------------------------------------------");
            System.out.println("1.계좌생성 | 2.계좌목록 | 3.예금 | 4.출금 | 5.종료");
            System.out.println("------------------------------------------------------------");
            System.out.print("선택> ");
            
            int select = sc.nextInt(); //1,2,3,4,5 중에 선택지 받기
            
            switch(select) {
            case(1):
            	createAccount(); //계좌 생성
            	break;
            case(2):
            	watchAccounts();//계좌 목록 보기
            	break;
            case(3):
            	deposit(); //예금
            	break;
            case(4):
            	withdraw(); //출금
            	break;
            case(5):
            	System.out.println("프로그램 종료");
        		run = false;
        		break;
            }
        }
        
    }
    
    public static void createAccount() {//계좌 생성
    	Account account = new Account("","",0); //일단 객체 생성
    	
    	sc.nextLine();//버퍼 초기화
    	
    	System.out.println("계좌번호: ");
    	account.setAno(sc.nextLine());
    	
    	System.out.println("계좌주: ");
    	account.setOwner(sc.nextLine());
    	
    	System.out.println("초기입금액: ");
    	account.setBalance(sc.nextInt());
    	
    	for (int i = 0; i < accountArray.length; i++) { //객체 배열에 저장
            if (accountArray[i] == null) {
                accountArray[i] = account;
                System.out.println("결과: 계좌가 생성되었습니다.");
                break;
            }
        }

    }
    
    public static void watchAccounts() {//계좌목록 출력
    	for (int i = 0; i < accountArray.length; i++) {
            if (accountArray[i] != null) {
            	System.out.println(accountArray[i].getAno()+"\t"+accountArray[i].getOwner()+"\t"+accountArray[i].getBalance());
            }
        }
    }
    
    public static void deposit() {
    	sc.nextLine();
    	
    	System.out.println("계좌번호: ");
    	String ano = sc.nextLine();
    	for(int i = 0; i< accountArray.length; i++) {
        	if(ano.equals(accountArray[i].getAno())) {
        		System.out.println("예금액: ");
        		int in = sc.nextInt();
        		accountArray[i].setBalance(accountArray[i].getBalance()+in);
        		break;
        	}
        	else {
        		System.out.println("해당 계좌가 없습니다.");
        		break;
        	}
    	}
    }
    public static void withdraw() {
    	
    	sc.nextLine();
    	System.out.println("계좌번호: ");
    	String ano = sc.nextLine();
    	for(int i = 0; i< accountArray.length; i++) {
        	if(ano.equals(accountArray[i].getAno())) {
        		System.out.println("출금액: ");
        		int in = sc.nextInt();
        		accountArray[i].setBalance(accountArray[i].getBalance()-in);
        		break;
        	}
        	else {
        		System.out.println("해당 계좌가 없습니다.");
        		break;
        	}
    	}
    }

   
}
    	 


