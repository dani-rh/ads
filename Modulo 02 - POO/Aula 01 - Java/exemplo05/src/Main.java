import java.sql.SQLOutput;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();

        if (idade < 18) {
            System.out.print("Voce é menor de idade");
        } else if(idade>=18 && idade<60){
                System.out.print("Voce é adulto.");
        } else{
            System.out.print("Voce é um(a) idoso(a).");
        }

        scanner.close();
    }
}