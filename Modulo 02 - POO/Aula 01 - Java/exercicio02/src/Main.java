import java.util.Scanner;

/*2. Crie um algoritmo em Java que verifica se um número inteiro
 é positivo, negativo ou zero.*/
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um número inteiro: ");
        int numero = scanner.nextInt();

        if (numero > 0){
            System.out.println("Número é positivo!");
        } else if (numero < 0) {
            System.out.println("Número é negativo!");
        }
        else{
            System.out.println("Número é zero!");
        }

        scanner.close();

    }
}