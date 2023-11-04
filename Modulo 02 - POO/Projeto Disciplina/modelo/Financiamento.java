package modelo;

public abstract class Financiamento{
    private double valorImovel;
    private int prazoFinanciamento;
    private double taxaJurosAnual;

    public Financiamento(double valorImovel, int prazoFinanciamento, double taxaJurosAnual){
        this.valorImovel = valorImovel;
        this.prazoFinanciamento = prazoFinanciamento;
        this.taxaJurosAnual = taxaJurosAnual;
    }

    public double getValorImovel(){
        return valorImovel;
    }

    public int getPrazoFinanciamento(){
        return prazoFinanciamento;
    }

    public double getTaxaJurosAnual(){
        return taxaJurosAnual;
    }

    // This method is now abstract and must be implemented by all subclasses
    public abstract double calcularPagamentoMensal();

    // This method uses the abstract method calcularPagamentoMensal but provides a concrete implementation
    public double calcularTotalPagamento(){
        return calcularPagamentoMensal() * (prazoFinanciamento * 12);
    }

    public void mostrarDadosFinanciamento(){
        System.out.println("Dados do Financiamento: ");
        System.out.println("Valor do Imóvel: " +valorImovel);
        System.out.println("Prazo de Financiamento: "+prazoFinanciamento+" anos");
        System.out.println("Taxa de Juros Anual: "+taxaJurosAnual+ "%");
    }
}
