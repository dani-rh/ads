import java.util.Random;

/*10. Crie um algoritmo em Java contendo a lógica do jogo da forca.
O programa deve escolher aleatoriamente uma palavra de uma lista de
palavras e o usuário deve adivinhar a palavra, uma letra de cada vez.
O usuário tem um número fixo de tentativas para adivinhar a palavra.
*/

import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] palavras = {"abacaxi", "banana", "laranja", "morango", "uva"};
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        String palavraSelecionada = palavras[random.nextInt(palavras.length)];
        int tentativas = 6;
        StringBuilder palavraAdivinhada = new StringBuilder();
        for (int i = 0; i < palavraSelecionada.length();i++){
            palavraAdivinhada.append("_");
        }

        System.out.println("Bem vindo ao jogo da Forca!");
        System.out.println("Tente adivinhar a palavra!");

        while(tentativas>0){
            System.out.println("Palavra: "+palavraAdivinhada);
            System.out.println("Tentativas restantes: "+tentativas);
            System.out.println("Digite uma letra: ");
            char letra = scanner.nextLine().charAt(0);
            boolean letraAdivinhada = false;

            for (int i = 0; i<palavraSelecionada.length();i++){
                if(palavraSelecionada.charAt(i) == letra){
                    palavraAdivinhada.setCharAt(i, letra);
                    letraAdivinhada = true;
                }
            }

            if(!letraAdivinhada){
                tentativas--;
            }

            if(palavraAdivinhada.toString().equals(palavraSelecionada)) {
                System.out.println("Parabéns! Voce adivinhou a palavra correta: " + palavraSelecionada);
                break;
            }
        }

        if(tentativas == 0){
            System.out.println("Game over! A palavra era: "+palavraSelecionada);
        }

        scanner.close();


    }
}