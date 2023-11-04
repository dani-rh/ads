package util;
import java.util.Scanner;

public class InterfaceUsuario {
    private Scanner scanner;

    public InterfaceUsuario(){
        scanner = new Scanner(System.in);
    }

    public double pedirValorImovel(){
        double valorImovel;
        do{
            System.out.println("Digite o valor do imóvel: ");
            valorImovel = scanner.nextDouble();
            if(valorImovel <= 0){
                System.out.println("Valor do imóvel deve ser positivo. Tente novamente:");
            }
        } while (valorImovel <=0);
        return valorImovel;
    }

    public int pedirPrazoFinanciamento(){
        int prazoFinanciamento;
        do{
            System.out.println("Digite o prazo do financiamento em anos: ");
            prazoFinanciamento = scanner.nextInt();
            if(prazoFinanciamento <= 0){
                System.out.println("Prazo do financiamento deve ser positivo. Tente novamente: ");
            }
        } while (prazoFinanciamento <=0);
        return prazoFinanciamento;
    }

    public double pedirTaxaDeJuros(){
        double taxaJurosAnual;
        do{
            System.out.println("Digite a taxa de juros anual (%): ");
            taxaJurosAnual = scanner.nextDouble();
            if(taxaJurosAnual <= 0){
                System.out.println("Taxa de juros anual deve ser positiva. Tente novamente: ");
            }
        } while (taxaJurosAnual <= 0);
        return taxaJurosAnual/100;
    }
}
