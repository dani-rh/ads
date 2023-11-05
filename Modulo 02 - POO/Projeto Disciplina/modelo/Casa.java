package modelo;

import java.io.Serializable;

public class Casa extends Financiamento implements Serializable {
    private static final double SEGURO_ADICIONAL = 80.0; // Valor fixo do seguro
    private double areaConstruida;
    private double tamanhoTerreno;

    public Casa(double valorImovel, int prazoFinanciamento, double taxaJurosAnual, double areaConstruida, double tamanhoTerreno) {
        super(valorImovel, prazoFinanciamento, taxaJurosAnual);
        this.areaConstruida = areaConstruida;
        this.tamanhoTerreno = tamanhoTerreno;
    }

    // Getters
    public double getAreaConstruida() {
        return areaConstruida;
    }

    public double getTamanhoTerreno() {
        return tamanhoTerreno;
    }

    // Setters
    public void setAreaConstruida(double areaConstruida) {
        this.areaConstruida = areaConstruida;
    }

    public void setTamanhoTerreno(double tamanhoTerreno) {
        this.tamanhoTerreno = tamanhoTerreno;
    }

    @Override
    public double calcularPagamentoMensal() {
        double taxaMensal = getTaxaJurosAnual() / 12;
        int meses = getPrazoFinanciamento() * 12;
        double pmt = getValorImovel() * (taxaMensal * Math.pow(1 + taxaMensal, meses)) / (Math.pow(1 + taxaMensal, meses) - 1);
        return pmt + SEGURO_ADICIONAL;
    }
}
