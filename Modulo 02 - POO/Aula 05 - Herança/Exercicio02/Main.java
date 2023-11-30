package Exercicio02;

public class Main {
    public static void main(String[] args) {
        ContaCorrente conta = new ContaCorrente("12345-6", 1000, 500);
        System.out.println("Saldo inicial: " + conta.getSaldo());
        System.out.println("Limite de crédito: " + conta.getLimiteDeCredito());

        double deposito = 500.0;
        double saque = 1500.0;

        System.out.println("Depositando: " + deposito);
        conta.depositar(deposito);
        System.out.println("Saldo após depósito: " + conta.getSaldo());

        System.out.println("Sacando: " + saque);
        conta.sacar(saque);
        System.out.println("Saldo após saque: " + conta.getSaldo());

        System.out.println("Sacando: " + saque);
        conta.sacar(saque);
        System.out.println("Saldo após saque exceder o limite: " + conta.getSaldo());
    }
}
