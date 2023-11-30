package Exercicio01;

public class Main {
    public static void main (String[] args){
        Livro livro = new Livro("1", "O Senhor dos Annéis", 59.99, "J.R.R. Tolkien", 1200);
        Eletronico eletronico = new Eletronico("2", "Samsung Galaxy S21", 5000, "Samsung", "Galaxy S21");
        Roupa roupa = new Roupa("3", "Camiseta Polo", 79.99, "M", "Azul");

    System.out.println("Livro: "+ livro.getNome() + ", Autor: "+livro.getAutor()+ ", Preço: "+livro.getPreco());
    System.out.println("Eletronico: " + eletronico.getNome() + ", Marca: " + eletronico.getMarca() + ", Preço: " + eletronico.getPreco());
    System.out.println("Roupa: " + roupa.getNome() + ", Tamanho: " + roupa.getTamanho() + ", Preço: " + roupa.getPreco());

    }
}
