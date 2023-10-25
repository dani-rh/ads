package Exercicio04.utilidades;
/*Crie um pacote chamado "utilidades". Dentro deste pacote, crie uma classe chamada "Calculadora" com métodos de pacote para operações básicas como soma, subtração, multiplicação e divisão. Todos os métodos precisam ser estáticos. Demonstre o funcionamento da classe ao Calculadora ao solicitar dois números para o usuário dentro de uma outra classe, chamada Main.
 */
public class Calculadora {
    public static int soma(int a, int b) {
        return a + b;
    }

    public static int subtrai(int a, int b) {
        return a - b;
    }

    public static int multiplica(int a, int b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Erro: Divisão por zero.");
            return Double.NaN;
        }
    }
}
