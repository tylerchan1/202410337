package chat;

import java.io.*;
import java.net.*;
import java.util.Scanner;

/**
실행 후:
1 서버가 요구하는 닉네임 입력
2 일반 메시지 입력 → 모두에게 전송
명령: /nick, /list, /w, /quit
 */
public class ChatClient {

    public static void main(String[] args) {
        String host = "127.0.0.1"; // 같은 PC면 로컬호스트
        int port = 5000; //포트 5000

        if (args.length >= 1) host = args[0];
        if (args.length >= 2) {
            try { port = Integer.parseInt(args[1]); } catch (NumberFormatException ignored) {}
        }

        try (Socket socket = new Socket(host, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
             PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true);
             Scanner scanner = new Scanner(System.in, "UTF-8")) {

            System.out.println("[CLIENT] Connected to " + host + ":" + port);

            // 수신 스레드: 서버에서 오는 모든 줄을 콘솔로 출력
            Thread reader = new Thread(() -> {
                try {
                    String line;
                    while ((line = in.readLine()) != null) {
                        System.out.println(line);
                    }
                } catch (IOException ignored) {
                } finally {
                    System.out.println("[CLIENT] Disconnected from server.");
                }
            });
            reader.setDaemon(true);
            reader.start();

            // 송신 루프: 콘솔 입력을 서버로 전송
            while (true) {
                if (!scanner.hasNextLine()) break;
                String line = scanner.nextLine();
                out.println(line);
                if ("/quit".equalsIgnoreCase(line.trim())) break;
            }

        } catch (IOException e) {
            System.err.println("[CLIENT] Error: " + e.getMessage());
        }
    }
}
