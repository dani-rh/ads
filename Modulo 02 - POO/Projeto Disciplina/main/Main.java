package main;

import modelo.Casa;
import modelo.Apartamento;
import modelo.Terreno;
import modelo.Financiamento;
import util.InterfaceUsuario;

import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.Locale;

public class Main {

    public static void main(String[] args) {

        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        ArrayList<Financiamento> financiamentos = new ArrayList<>();

        String[] tiposImovel = {"Casa", "Casa", "Apartamento", "Apartamento", "Terreno"};
        // Adicionar dois financiamentos de casa, dois de apartamento e um de terreno
        for (int i = 0; i < 5; i++) {
            System.out.println("Financiamento " + (i + 1) + " - " + tiposImovel[i]);
            double valorImovel = interfaceUsuario.pedirValorImovel();
            int prazoFinanciamento = interfaceUsuario.pedirPrazoFinanciamento();
            double taxaJurosAnual = interfaceUsuario.pedirTaxaDeJuros();

            Financiamento financiamento;
            if (i < 2) {
                double areaConstruida = interfaceUsuario.pedirAreaConstruida();
                double tamanhoTerreno = interfaceUsuario.pedirTamanhoTerreno();
                financiamento = new Casa(valorImovel, prazoFinanciamento, taxaJurosAnual, areaConstruida, tamanhoTerreno);
            } else if (i < 4) {
                int numeroVagasGaragem = interfaceUsuario.pedirNumeroVagasGaragem();
                int numeroAndar = interfaceUsuario.pedirNumeroAndar();
                financiamento = new Apartamento(valorImovel, prazoFinanciamento, taxaJurosAnual, numeroVagasGaragem, numeroAndar);
            } else {
                String tipoZona = interfaceUsuario.pedirTipoZona();
                financiamento = new Terreno(valorImovel, prazoFinanciamento, taxaJurosAnual, tipoZona);
            }
            financiamentos.add(financiamento);
        }
        
        interfaceUsuario.closeScanner();
        // Calcular e mostrar os totais
        double totalImoveis = 0;
        double totalFinanciamentos = 0;

        for (Financiamento financiamento : financiamentos) {
            double valorImovel = financiamento.getValorImovel();
            double valorFinanciamento = financiamento.calcularTotalPagamento();

            System.out.println("Financiamento " + (financiamentos.indexOf(financiamento) +1) +
                    " - valor do imóvel: " + formatarMoeda(valorImovel) +
                    ", valor do financiamento: " + formatarMoeda(valorFinanciamento));

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
