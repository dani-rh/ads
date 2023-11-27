package main;

import modelo.Casa;
import modelo.Apartamento;
import modelo.Terreno;
import modelo.Financiamento;
import util.InterfaceUsuario;

import java.io.*;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.Locale;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {

    public static void main(String[] args) {
        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        ArrayList<Financiamento> financiamentos = new ArrayList<>();

        String[] tiposImovel = {"Casa", "Casa", "Apartamento", "Apartamento", "Terreno"};
        for (int i = 0; i < tiposImovel.length; i++) {
            System.out.println("Financiamento " + (i + 1) + " - " + tiposImovel[i]);
            double valorImovel = interfaceUsuario.pedirValorImovel();
            int prazoFinanciamento = interfaceUsuario.pedirPrazoFinanciamento();
            double taxaJurosAnual = interfaceUsuario.pedirTaxaDeJuros();

            Financiamento financiamento;
            if ("Casa".equals(tiposImovel[i])) {
                double areaConstruida = interfaceUsuario.pedirAreaConstruida();
                double tamanhoTerreno = interfaceUsuario.pedirTamanhoTerreno();
                financiamento = new Casa(valorImovel, prazoFinanciamento, taxaJurosAnual, areaConstruida, tamanhoTerreno);
            } else if ("Apartamento".equals(tiposImovel[i])) {
                int numeroVagasGaragem = interfaceUsuario.pedirNumeroVagasGaragem();
                int numeroAndar = interfaceUsuario.pedirNumeroAndar();
                financiamento = new Apartamento(valorImovel, prazoFinanciamento, taxaJurosAnual, numeroVagasGaragem, numeroAndar);
            } else {
                String tipoZona = interfaceUsuario.pedirTipoZona();
                financiamento = new Terreno(valorImovel, prazoFinanciamento, taxaJurosAnual, tipoZona);
            }
            financiamentos.add(financiamento);
            salvarFinanciamentosEmArquivo(financiamentos);
            lerFinanciamentosDoArquivo();
        }

        // Serializar lista de financiamentos
        serializeFinanciamentos(financiamentos);

        ArrayList<Financiamento> deserializedFinanciamentos = deserializeFinanciamentos();
        if (deserializedFinanciamentos != null) {
            double totalImoveis = 0;
            double totalFinanciamentos = 0;

            for (Financiamento financiamento : deserializedFinanciamentos) {
                double valorImovel = financiamento.getValorImovel();
                double valorFinanciamento = financiamento.calcularTotalPagamento();
                System.out.println("Financiamento " + (deserializedFinanciamentos.indexOf(financiamento) + 1) +
                        " - valor do imóvel: " + formatarMoeda(valorImovel) +
                        ", valor do financiamento: " + formatarMoeda(valorFinanciamento));

                totalImoveis += valorImovel;
                totalFinanciamentos += valorFinanciamento;
            }

            System.out.println("Total de todos os imóveis: " + formatarMoeda(totalImoveis));
            System.out.println("Total de todos os financiamentos: " + formatarMoeda(totalFinanciamentos));
        }

        interfaceUsuario.closeScanner();
    }

    public static void serializeFinanciamentos(ArrayList<Financiamento> financiamentos) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("financiamentos.ser"))) {
            oos.writeObject(financiamentos);
            System.out.println("Financiamentos serializados com sucesso.");
        } catch (IOException e) {
            System.out.println("Erro ao serializar financiamentos: " + e.getMessage());
        }
    }

    @SuppressWarnings("unchecked")
    public static ArrayList<Financiamento> deserializeFinanciamentos() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("financiamentos.ser"))) {
            return (ArrayList<Financiamento>) ois.readObject();
        } catch (IOException e) {
            System.out.println("Erro ao deserializar financiamentos: " + e.getMessage());
            return null;
        } catch (ClassNotFoundException e) {
            System.out.println("Classe não encontrada durante a deserialização: " + e.getMessage());
            return null;
        }
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

    //Salvar em arquivo
    public static void salvarFinanciamentosEmArquivo(ArrayList<Financiamento> financiamentos) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("financiamentos.txt"))) {
            for (Financiamento financiamento : financiamentos) {
                String line = createLineForFinanciamento(financiamento);
                writer.write(line);
                writer.newLine();
            }
            System.out.println("Financiamentos salvos em arquivo.");
        } catch (IOException e) {
            System.out.println("Erro ao escrever no arquivo: " + e.getMessage());
        }
    }
    private static String createLineForFinanciamento(Financiamento financiamento) {
        String line = financiamento.getValorImovel() + "; " +
                      financiamento.calcularTotalPagamento() + "; " +
                      financiamento.getTaxaJurosAnual() + "; " +
                      financiamento.getPrazoFinanciamento();
        if (financiamento instanceof Casa) {
            Casa casa = (Casa) financiamento;
            line += "; " + casa.getAreaConstruida() + "; " + casa.getTamanhoTerreno();
        } else if (financiamento instanceof Apartamento) {
            Apartamento apartamento = (Apartamento) financiamento;
            line += "; " + apartamento.getNumeroVagasGaragem() + "; " + apartamento.getNumeroAndar();
        } else if (financiamento instanceof Terreno) {
            Terreno terreno = (Terreno) financiamento;
            line += "; " + terreno.getTipoZona();
        }
        return line;
    }
    public static void lerFinanciamentosDoArquivo() {
        try {
            Files.readAllLines(Paths.get("financiamentos.txt")).forEach(System.out::println);
            System.out.println("Leitura do arquivo de financiamentos completa.");
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        }
    }
}
