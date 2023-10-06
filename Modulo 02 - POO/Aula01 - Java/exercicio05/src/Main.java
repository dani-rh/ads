import java.util.Scanner;

/*5. Crie um algoritmo em Java que peça ao usuário para que se
digite um ano (exemplo: 2032). Em seguida, o algoritmo deve verificar
se o ano informado é ou não bissexto.*/
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um ano: ");
        int ano = scanner.nextInt();

        boolean bissexto = false;

        if(ano % 4 == 0){
            if(ano % 100 == 0){
                if (ano % 400 == 0){
                    bissexto = true;
                }
            }else{
                bissexto = true;
            }
        }
        if(bissexto){
            System.out.println("O ano é bissexto.");
        }else{
            System.out.println("O ano não é bissexto.");
        }
        scanner.close();
    }
}