package Exercicio02;

import java.util.ArrayList;
import java.util.function.DoubleToIntFunction;

import javax.sound.sampled.SourceDataLine;

public class CarrinhoDeCompras {
    private ArrayList produtos;

    public CarrinhoDeCompras(){
        this.produtos = new ArrayList();
    }

    public void adicionarProduto(Produto produto){
        produto.decrementarEstoque();
        this.produtos.add(produto);
    }

    public void removerProduto(Produto produto){
        this.produtos.remove(produto);
    }

    public double calcularTotal(){
        double total = 0.0;
        for (Produto produto : this.produtos){
            total += produto.getPreco();
        }
        return total;
    }

    public static void main(String[] args) {
         Produto produto1 = new Produto("TV", 1200.00, 10);
         Produto produto2 = new Produto("Laptop", 2500.00, 5);
         Produto produto3 = new Produto("Celular", 800.00, 20);
 
         CarrinhoDeCompras carrinho = new CarrinhoDeCompras();
         System.out.println("Total do Carrinho no início: " + carrinho.calcularTotal());
 
         carrinho.adicionarProduto(produto1);
         carrinho.adicionarProduto(produto2);
         carrinho.adicionarProduto(produto3);
 
         System.out.println("Total do Carrinho depois de adicionar: " + carrinho.calcularTotal());
 
         carrinho.removerProduto(produto2);
 
         System.out.println("Total do Carrinho após remover o produto: " + carrinho.calcularTotal());
     }
}
