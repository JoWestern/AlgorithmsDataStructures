
/*  Denne klassen er laget ut fra oppgaveteksten til Datastrukturer oppg. 3 i Assignment 1.
 *   Oppgaveteksten gjorde det noe forvirrende anngående start og end ettersom de satt fast på verdien 0,
 *   jeg gjorde en endring for at det itereres med riktig index i arrayen buf.
 */
public class DataStructure {
    int n = 100, start = 0, end = 0;
    int[] buf = new int[n];

    public void put(int item) {
        buf[end] = item;
        end = end + 1;
        end = end % n;
    }

    public int get() {
        int item = buf[start];
        start = start + 1;
        start = start % n;

        return item;
    }
}
