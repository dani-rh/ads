public class Main {
    public static void main(String[] args) {
        int numero = 3;

        if (numero == 1) {
            System.out.println("O número é igual a 1");
        } else if (numero == 2) {
            System.out.println("O número é igual a 2");
        } else if (numero == 3) {
            System.out.println("O número é igual a 3");
        } else {
            System.out.println("O número é diferente de 1, 2 e 3");
        }
    }
}

//Usando o switch
public class Exemplo {
    public static void main(String[] args) {
        int numero = 3;

        switch (numero) {
            case 1:
                System.out.println("O número é igual a 1");
                break;
            case 2:
                System.out.println("O número é igual a 2");
                break;
            case 3:
                System.out.println("O número é igual a 3");
                break;
            default:
                System.out.println("O número é diferente de 1, 2 e 3");
                break;
        }
    }
}