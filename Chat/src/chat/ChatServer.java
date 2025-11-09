package chat;

import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.*;

/**
 * 콘솔 채팅 서버 (멀티 클라이언트)
 * 명령:
 *  /nick 새닉네임   - 닉네임 변경
 *  /list            - 현재 유저 목록
 *  /w 닉 메시지     - 해당 닉네임에게 귓속말
 *  /quit            - 종료
 */
public class ChatServer {

    private final int port;
    private final ServerSocket serverSocket;

    // 닉네임 -> 핸들러
    private final ConcurrentMap<String, ClientHandler> clients = new ConcurrentHashMap<>();

    public ChatServer(int port) throws IOException {
        this.port = port;
        this.serverSocket = new ServerSocket(port);
        this.serverSocket.setReuseAddress(true);
    }

    public void start() {
        log("Server listening on port " + port);
        try {
            while (true) {
                Socket socket = serverSocket.accept();
                socket.setTcpNoDelay(true);
                new Thread(new ClientHandler(socket)).start();
            }
        } catch (IOException e) {
            log("Server stopped: " + e.getMessage());
        } finally {
            try { serverSocket.close(); } catch (IOException ignored) {}
        }
    }

    private void broadcast(String from, String message) {
        String line = (from == null ? "[SERVER]" : "[" + from + "]") + " " + message;
        for (ClientHandler ch : clients.values()) {
            ch.send(line);
        }
        System.out.println(line);
    }

    private static void log(String msg) {
        System.out.println("[SERVER] " + msg);
    }

    private class ClientHandler implements Runnable {
        private final Socket socket;
        private String nickname = null;
        private PrintWriter out;
        private BufferedReader in;

        ClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            String remote = socket.getRemoteSocketAddress().toString();
            log("Connected: " + remote);
            try (socket) {
                out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true);
                in  = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));

                // 1) 닉네임 확보(중복 불가)
                requestNickname();

                // 2) 입장 알림
                broadcast(null, nickname + " joined. (" + clients.size() + " users)");

                // 3) 메시지 루프
                String line;
                while ((line = in.readLine()) != null) {
                    line = line.trim();
                    if (line.isEmpty()) continue;

                    if (line.startsWith("/")) {
                        handleCommand(line);
                    } else {
                        broadcast(nickname, line);
                    }
                }
            } catch (IOException e) {
                log("IO error: " + e.getMessage());
            } finally {
                if (nickname != null) {
                    clients.remove(nickname);
                    broadcast(null, nickname + " left. (" + clients.size() + " users)");
                }
                log("Disconnected: " + remote);
            }
        }

        private void requestNickname() throws IOException {
            send("Welcome to ConsoleChat!");
            send("Commands: /nick, /list, /w, /quit");
            while (true) {
                send("Enter your nickname:");
                String tryNick = in.readLine();
                if (tryNick == null) throw new IOException("Client closed");
                tryNick = tryNick.trim();
                if (tryNick.isEmpty()) {
                    send("Nickname cannot be empty.");
                    continue;
                }
                if (tryNick.contains(" ") || tryNick.startsWith("/")) {
                    send("Invalid nickname. No spaces or '/' allowed.");
                    continue;
                }
                if (clients.putIfAbsent(tryNick, this) == null) {
                    this.nickname = tryNick;
                    send("Hello, " + nickname + "!");
                    break;
                } else {
                    send("Nickname already in use. Try another.");
                }
            }
        }

        private void handleCommand(String cmdLine) {
            String[] parts = cmdLine.split("\\s+", 3);
            String cmd = parts[0].toLowerCase();

            switch (cmd) {
                case "/quit":
                    send("Bye!");
                    // 소켓 종료 → finally에서 정리
                    try { socket.close(); } catch (IOException ignored) {}
                    break;

                case "/list":
                    send("Users: " + String.join(", ", clients.keySet()));
                    break;

                case "/nick":
                    if (parts.length < 2) {
                        send("Usage: /nick NEW_NAME");
                        break;
                    }
                    String newNick = parts[1].trim();
                    if (newNick.isEmpty() || newNick.contains(" ") || newNick.startsWith("/")) {
                        send("Invalid nickname.");
                        break;
                    }
                    if (clients.containsKey(newNick)) {
                        send("Nickname already in use.");
                        break;
                    }
                    // 변경
                    clients.remove(this.nickname);
                    clients.put(newNick, this);
                    String old = this.nickname;
                    this.nickname = newNick;
                    broadcast(null, old + " is now known as " + newNick);
                    break;

                case "/w":
                    if (parts.length < 3) {
                        send("Usage: /w USER MESSAGE");
                        break;
                    }
                    String target = parts[1];
                    String msg = parts[2];
                    ClientHandler dst = clients.get(target);
                    if (dst == null) {
                        send("User not found: " + target);
                    } else {
                        dst.send("[WHISPER from " + nickname + "] " + msg);
                        send("[WHISPER to " + target + "] " + msg);
                    }
                    break;

                default:
                    send("Unknown command: " + cmd);
            }
        }

        private void send(String msg) {
            if (out != null) {
                out.println(msg);
            }
        }
    }

    public static void main(String[] args) {
        int port = 5000;
        if (args.length >= 1) {
            try { port = Integer.parseInt(args[0]); } catch (NumberFormatException ignored) {}
        }
        try {
            new ChatServer(port).start();
        } catch (IOException e) {
            System.err.println("Failed to start: " + e.getMessage());
        }
    }
}
