package Exemplo07;

public class Bar extends Foo{
    public void a() {
        System.out.println("A");
    }
    
    public static void main(String[] args) {
        Foo f = new Bar();
        f.print();
    }
}
