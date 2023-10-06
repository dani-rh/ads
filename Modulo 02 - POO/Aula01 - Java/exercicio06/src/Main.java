import java.util.Scanner;

/*6. Crie um algoritmo em Java que solicita um número inteiro ao usuário.
 Em seguida, deve-se verificar se o número digitado é ou não é um número primo.
*/
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um número: ");
        int numero = scanner.nextInt();

        boolean primo = true;

        if(numero <=1){
            primo = false;
        }else{
            for(int i = 2; i <= Math.sqrt(numero);i++){
                if(numero%i == 0){
                    primo = false;
                    break;
                }
            }
        }

        if(primo){
            System.out.println("O número é primo");
        }else{
            System.out.println("O número não é primo.");
        }

        scanner.close();
    }
}