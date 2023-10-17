package exercicio06;

import java.util.ArrayList;
 
 public class Serie {
     // Atributos da classe Serie
     String nome;
ArrayList episodios;
 
     // Método construtor da classe Serie
     Serie(String nome) {
         this.nome = nome;
         this.episodios = new ArrayList<>();
     }
 
     // Método para adicionar episódio à série
     void adicionarEpisodio(Episodio episodio) {
         this.episodios.add(episodio);
     }
 
     // Método para imprimir as informações da série
     void imprimirInfoSerie() {
         System.out.println("Série: " + this.nome);
         System.out.println("Episódios:");
         for(Episodio episodio : this.episodios) {
             episodio.imprimirInfoEpisodio();
         }
     }
 
     // Método principal
     public static void main(String[] args) {
         // Criação de instâncias de Episódio
         Episodio episodio1 = new Episodio("Episódio 1", 45);
         Episodio episodio2 = new Episodio("Episódio 2", 52);
         Episodio episodio3 = new Episodio("Episódio 3", 49);
 
         // Criação de uma instância de Serie
         Serie serie = new Serie("Série 1");
 
         // Adicionando episódios a uma Serie
         serie.adicionarEpisodio(episodio1);
         serie.adicionarEpisodio(episodio2);
         serie.adicionarEpisodio(episodio3);
 
         // Adicionando episódios de um outro jeito
         serie.adicionarEpisodio(new Episodio("Episódio 4", 64));
         serie.adicionarEpisodio(new Episodio("Episódio 5", 55));
 
         // Mostrando as informações da Serie
         serie.imprimirInfoSerie();
     }
}
