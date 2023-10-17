package exercicio06;

import java.util.ArrayList;
 
 public class Usuario {
// Atributos da classe
     String nome;
     String email;
     String senha;
ArrayList seriesAssistidas;
 
// Método construtor
     Usuario(String nome, String email, String senha) {
         this.nome = nome;
         this.email = email;
         this.senha = senha;
this.seriesAssistidas = new ArrayList<>(); // iniciando uma lista vazia
     }
 
// Método para imprimir as informações do usuário
     void imprimirInfo() {
System.out.println("Nome: " + this.nome);
System.out.println("Email: " + this.email);
System.out.println("Séries assistidas:");
         for(Serie serie : this.seriesAssistidas) {
             serie.imprimirInfoSerie();
         }
System.out.println("\n\n");
     }
 
     boolean adicionarSerieAoHistorico(Serie serie) {
// Verificamos antes se a série já existe no histórico
         if (this.seriesAssistidas.contains(serie)) {
             return false;
         } else {
             this.seriesAssistidas.add(serie);
             return true;
         }
     }
 
// Método para verificar se uma senha fornecida é a senha correta do usuário
     boolean verificarSenha(String senhaFornecida) {
         return this.senha.equals(senhaFornecida);
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
 
         // Criação de uma instância de Usuario
         Usuario usuario = new Usuario("João", "joao@exemplo.com", "senhaSegura123");
 
         // Impressão das informações do usuário
         usuario.imprimirInfo();
 
         // Adicionando uma série assistida ao histórico do usuário
         usuario.adicionarSerieAoHistorico(serie);
 
         // Impressão das informações do usuário
         usuario.imprimirInfo();
     }
 }