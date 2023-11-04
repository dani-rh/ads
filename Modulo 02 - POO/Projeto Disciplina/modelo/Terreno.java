package modelo;

public class Terreno extends Financiamento {
    private static final double ACRESCIMO_INADIMPLENCIA = 0.02; // 2% de acréscimo

    public Terreno(double valorImovel, int prazoFinanciamento, double taxaJurosAnual) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
    }

    @Override
    public double calcularPagamentoMensal() {
        // Chama o método da superclasse e adiciona o acréscimo de inadimplência
        double pagamentoComJuros = super.calcularPagamentoMensal();
        return pagamentoComJuros * (1 + ACRESCIMO_INADIMPLENCIA);
    }
}