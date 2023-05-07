// Kort test for å demonstrere programmet

public class Main {
    public static void main(String[] args) {
        DataStructure d = new DataStructure();
        d.put(1);
        d.put(3);
        d.put(3);
        d.put(4);

        for (int i=0; i<4; i++) {
            System.out.println(d.get());
        }
    }
}
