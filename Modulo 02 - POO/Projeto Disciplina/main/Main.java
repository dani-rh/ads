package main;

import modelo.Financiamento;
import util.InterfaceUsuario;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.Locale;

public class Main {
    
    public static void main(String[] args){

        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        ArrayList<Financiamento> financiamentos = new ArrayList<>();

        //Adicionar 4 financiamentos ao ArrayList - usar forloop
        for(int i = 0; i < 1; i++){
            System.out.println("Financiamento "+ (i+1));
            double valorImovel = interfaceUsuario.pedirValorImovel();
            int prazoFinanciamento = interfaceUsuario.pedirPrazoFinanciamento();
            double taxaJurosAnual =  interfaceUsuario.pedirTaxaDeJuros();

            Financiamento financiamento = new Financiamento(valorImovel, prazoFinanciamento, taxaJurosAnual);
            financiamentos.add(financiamento);
        }

        //Calcular e mostrar os totais
        double totalImoveis = 0;
        double totalFinanciamentos = 0;
        DecimalFormat df = new DecimalFormat("R$ #,##0.00");

        for(int i = 0; i<financiamentos.size(); i++){
            Financiamento financiamento = financiamentos.get(i);
            double valorImovel = financiamento.getValorImovel();
            double valorFinanciamento = financiamento.calcularTotalPagamento();

            System.out.println("Financiamento " +  (i + 1) + " - valor do imóvel: " + formatarMoeda(valorImovel) +
                                ", valor do financiamento: "+ formatarMoeda(valorFinanciamento));
            
            totalImoveis += valorImovel;
            totalFinanciamentos += valorFinanciamento;
        }
        System.out.println("Total de todos os imóveis: " + formatarMoeda(totalImoveis));
        System.out.println("Total de todos os financiamentos: " + formatarMoeda(totalFinanciamentos));
    }

    public static String formatarMoeda(double value) {
        Locale ptBR = Locale.forLanguageTag("pt-BR");
        DecimalFormatSymbols symbols = new DecimalFormatSymbols(ptBR);
        symbols.setDecimalSeparator(',');
        symbols.setGroupingSeparator('.');
        
        DecimalFormat df = new DecimalFormat("R$ #,##0.00", symbols);
        df.setDecimalFormatSymbols(symbols);
        
        return df.format(value);
    }

}
