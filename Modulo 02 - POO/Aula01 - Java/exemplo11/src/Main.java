
public class Main {
    public static void main(String[] args) {
        int[] numeros = {1, 2, 3, 4, 5};

        System.out.println("Exemplo com o loop for:");
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Número: " + numeros[i]);
        }

        System.out.println("\n\nExemplo com o loop foreach:");
        for (int numero : numeros) {
            System.out.println("Número: " + numero);
        }
    }
}