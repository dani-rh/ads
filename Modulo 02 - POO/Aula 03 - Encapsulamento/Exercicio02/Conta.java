package Exercicio02;
/*Crie uma classe "Conta" que tenha um membro privado "saldo" (double) e um membro público "numero" (int). Crie métodos públicos para depositar e sacar dinheiro da conta (ajustando o saldo adequadamente). Certifique-se de que o saldo não pode se tornar negativo através de saques. Além disso, crie um método público para obter o saldo da conta.
 */
class Conta {
    private double saldo;

    public int numero;

    public Conta(int numero, double saldoInicial) {
        this.numero = numero;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
        } else {
            System.out.println("O valor do depósito deve ser positivo.");
        }
    }

    public void sacar(double valor) {
        if (valor > saldo) {
            System.out.println("Saldo insuficiente para realizar o saque.");
        } else if (valor <= 0) {
            System.out.println("O valor de saque deve ser positivo.");
        } else {
            saldo -= valor;
        }
    }

    public double getSaldo() {
        return saldo;
    }
}

public class Main {
    public static void main(String[] args) {
        Conta minhaConta = new Conta(12345, 1000.0);

        minhaConta.depositar(500.0);
        System.out.println("Saldo atual: " + minhaConta.getSaldo());

        minhaConta.sacar(300.0);
        System.out.println("Saldo atual: " + minhaConta.getSaldo());

        minhaConta.sacar(1500.0);
        System.out.println("Saldo atual: " + minhaConta.getSaldo());
    }
}
