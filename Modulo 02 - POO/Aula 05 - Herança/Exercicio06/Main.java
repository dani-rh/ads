package Exercicio06;

public class Main {
    public static void main(String[] args) {

        CarrinhoDeCompras carrinho = new CarrinhoDeCompras();
 
         // Adicionando um Perfume e uma Maquiagem no carrinho
         carrinho.adicionarProduto(new Perfume("Perfume ABC", "Floral"));
         carrinho.adicionarProduto(new Maquiagem("Maquiagem DEF", "Vermelho"));
 
         // Obtendo o primeiro produto do carrinho (que é um Perfume)
         Produto produto = carrinho.getProduto(0);
 
         // Usando typecasting para tratar o produto como Perfume
         if (produto instanceof Perfume) {
             Perfume perfume = (Perfume) produto;
             System.out.println("Nome do perfume: " + perfume.getNome());
             System.out.println("Fragrância do perfume: " + perfume.getFragrancia());
         }
     }
}
