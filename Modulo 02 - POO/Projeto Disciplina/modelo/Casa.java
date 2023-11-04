package modelo;

public class Casa extends Financiamento {
    private static final double SEGURO_ADICIONAL = 80.0; // Valor fixo do seguro

    public Casa(double valorImovel, int prazoFinanciamento, double taxaJurosAnual) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
    }

    @Override
    public double calcularPagamentoMensal() {
        // Chama o método da superclasse e adiciona o seguro
        return super.calcularPagamentoMensal() + SEGURO_ADICIONAL;
    }
}
