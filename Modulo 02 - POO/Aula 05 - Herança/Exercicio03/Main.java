package Exercicio03;

public class Main {
    public static void main(String[] args) {
        Casa casa = new Casa();
        System.out.println("Preço por noite para Casa: " + casa.precoPorNoite());

        Apartamento apartamento = new Apartamento();
        System.out.println("Preço por noite para Apartamento: " + apartamento.precoPorNoite());
    }
}
