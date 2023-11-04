package modelo;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

import javax.sound.sampled.SourceDataLine;

public class Financiamento{
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

    public double calcularPagamentoMensal(){
        return (valorImovel/prazoFinanciamento) * (1 + (taxaJurosAnual/12));
    }

    public double calcularTotalPagamento(){
        return calcularPagamentoMensal() * prazoFinanciamento;
    }

    public void mostrarDadosFinanciamento(){
        System.out.println("Dados do Financiamento: ");
        System.out.println("Valor do Imóvel: " +valorImovel);
        System.out.println("Prazo de Financiamento: "+prazoFinanciamento+" anos");
        System.out.println("Taxa de Juros Anual: "+taxaJurosAnual+ "%");
    }
}