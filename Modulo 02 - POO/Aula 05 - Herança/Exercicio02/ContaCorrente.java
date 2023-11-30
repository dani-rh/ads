package Exercicio02;

public class ContaCorrente extends ContaBancaria{
    private double limiteDeCredito;

    public ContaCorrente (String numeroDaConta, double saldoInicial, double limiteDeCredito){
        super(numeroDaConta, saldoInicial);
        this.limiteDeCredito = limiteDeCredito;
    }

    public double getLimiteDeCredito(){
        return this.limiteDeCredito;
    }

    @Override
    public void sacar(double valor){
        if (valor > saldo + limiteDeCredito){
            System.out.println("Saldo insuficiente para saque.");
        } else{
            this.saldo -= valor;
        }
    }
}
