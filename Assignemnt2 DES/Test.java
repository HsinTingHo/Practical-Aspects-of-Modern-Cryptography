
public class Test{
	public static void main(String[] args) {
		//System.out.println("");
		String msg = "msg";
		String k = "key";
		DES des = new DES(msg, k);
		Public_Tables pt = new Public_Tables();
		pt.test();
	}
}