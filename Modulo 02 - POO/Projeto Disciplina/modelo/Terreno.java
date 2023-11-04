package modelo;

public class Terreno extends Financiamento {
    private static final double ACRESCIMO_INADIMPLENCIA = 0.02; // 2% de acréscimo
    private String tipoZona;

    public Terreno(double valorImovel, int prazoFinanciamento, double taxaJurosAnual, String tipoZona) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
        this.tipoZona = tipoZona;
    }
    
    // Getters
    public String getTipoZona() {
        return tipoZona;
    }

    // Setters
    public void setTipoZona(String tipoZona) {
        this.tipoZona = tipoZona;
    }

    @Override
    public double calcularPagamentoMensal() {
        double taxaMensal = getTaxaJurosAnual() / 12;
        int meses = getPrazoFinanciamento() * 12;
        double pmt = getValorImovel() * (taxaMensal * Math.pow(1 + taxaMensal, meses)) / (Math.pow(1 + taxaMensal, meses) - 1);
        return pmt * (1 + ACRESCIMO_INADIMPLENCIA);
    }
}
