/* 1. Crie um algoritmo em Java que solicita três números decimais ao usuário.
Em seguida, a média destes números é calculada e mostrada na tela para o usuário.*/
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o primeiro número decimal: ");
        double num1 = scanner.nextDouble();
        System.out.println("Digite o segundo número decimal: ");
        double num2 = scanner.nextDouble();
        System.out.println("Digite o terceiro número decimal: ");
        double num3 = scanner.nextDouble();

        double media = (num1 + num2 + num3)/3;

        System.out.println("A média dos números é: "+media);

        scanner.close();

    }
}