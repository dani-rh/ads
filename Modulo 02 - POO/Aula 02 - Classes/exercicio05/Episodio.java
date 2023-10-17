package exercicio05;

public class Episodio {
        //Atributo da classe
        private String titulo;
        private int duracao;
    
        //Método construtor da classe
        public Episodio(String titulo, int duracao){
            this.titulo = titulo;
            this.duracao = duracao;
        }
    
        //Método para imprimir
        public void imprimirInfoEpisodio(){
            System.out.println("Titulo: "+this.titulo);
            System.out.println("Duração: "+this.duracao+ " minutos.");
        }
    
    // Método principal
    public static void main(String[] args) {
        // Criação de instâncias de Episódio
        Episodio episodio1 = new Episodio("Episódio 1", 45);
        Episodio episodio2 = new Episodio("Episódio 2", 52);
        Episodio episodio3 = new Episodio("Episódio 3", 49);
        Episodio episodio4 = new Episodio("Episódio 4", 64);
        Episodio episodio5 = new Episodio("Episódio 5", 55);
    
        // Mostrando as informações de um Episódio como exemplo
        episodio4.imprimirInfoEpisodio();
    }
}
