package Exercicio04;

 import java.util.Scanner;
 import Exercicio04.utilidades.Calculadora;

 public class Main {
    public static void main(String[] args) {
 
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int num1 = scanner.nextInt();

        System.out.print("Digite o segundo número: ");
        int num2 = scanner.nextInt();

        System.out.println("Soma: " + Calculadora.soma(num1, num2));
        System.out.println("Subtração: " + Calculadora.subtrai(num1, num2));
        System.out.println("Multiplicação: " + Calculadora.multiplica(num1, num2));
        System.out.println("Divisão: " + Calculadora.divide(num1, num2));
    }
}
