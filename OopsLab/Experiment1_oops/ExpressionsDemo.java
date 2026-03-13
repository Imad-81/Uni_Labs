public class ExpressionsDemo {

   public static void main(String[] args) {

       int a = (101 + 0) / 3;

       System.out.println("(101 + 0) / 3 = " + a);

       double b = 3.0e-6 * 10000000.1;

       System.out.println("(3.0e-6 * 10000000.1) = " + b);

        boolean t = true;
        boolean f = false;

        boolean c = (t && true);

        System.out.println("(true && true) = " + c);

        boolean d = (f && true);

        System.out.println("(false && true) = " + d);

        boolean e = (f && (f || t));

        System.out.println("(false && (false || true)) = " + e);

        boolean ff = (f || f) && (t && t);

        System.out.println("((false || false) && (true && true)) = " + ff);

   }

}