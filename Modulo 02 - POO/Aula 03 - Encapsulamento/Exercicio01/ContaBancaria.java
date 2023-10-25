package Exercicio01;
/*Crie uma classe "ContaBancaria" com atributos privados para "numeroDaConta", "agencia", "saldo" e "senha". Use métodos getter para "agencia", "numeroDaConta" e "saldo", mas apenas um método setter para "senha".
 */
public class ContaBancaria {
    private String numeroDaConta;    
    private String agencia;
    private double saldo;
    private String senha;

    public ContaBancaria(String numeroDaConta, String agencia,
    double saldo, String senha){
        this.numeroDaConta = numeroDaConta;
        this.agencia = agencia;
        this.saldo = saldo;
        this.senha = senha;
    }

    public String getAgencia(){
        return agencia;
    }
    public String getNumeroDaConta(){
        return numeroDaConta;
    }
    public double getSaldo(){
        return saldo;
    }
    public void setSenha(String senha){
        this.senha = senha;
    }

    public static void main(String[] args) {
        ContaBancaria conta1 = new ContaBancaria("1234", "001", 1000.00, "senha123");
        System.out.println("Conta 1 - Número: " + conta1.getAgencia() + ", " + conta1.getNumeroDaConta() + ", Saldo: R$" + conta1.getSaldo());

        ContaBancaria conta2 = new ContaBancaria("5678", "002", 2000.00, "senha456");
        System.out.println("Conta 2 - Número: " + conta2.getAgencia() + ", " + conta2.getNumeroDaConta() + ", Saldo: R$" + conta2.getSaldo());

        ContaBancaria conta3 = new ContaBancaria("9012", "003", 3000.00, "senha789");
        System.out.println("Conta 3 - Número: " + conta3.getAgencia() + ", " + conta3.getNumeroDaConta() + ", Saldo: R$" + conta3.getSaldo());
    }
}
