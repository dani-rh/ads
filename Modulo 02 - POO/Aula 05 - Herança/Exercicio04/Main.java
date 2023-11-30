package Exercicio04;

public class Main {
    public static void main(String[] args) {
        Viagem viagem = new Viagem();

        double preco = viagem.calcularPreco(10); // distância de 10km
        System.out.println("O preço da viagem é: " + preco);

        preco = viagem.calcularPreco(10, true); // distância de 10km em horário de pico
        System.out.println("O preço da viagem em horário de pico é: " + preco);
    }
}
