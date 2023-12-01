package Exercicio06;

import java.util.ArrayList;

class CarrinhoDeCompras{
    private ArrayList produtos;
 
    public CarrinhoDeCompras() {
        this.produtos = new ArrayList();
    }
 
    public void adicionarProduto(Produto produto) {
        this.produtos.add(produto);
    }
 
    public Produto getProduto(int index) {
        return produtos.get(index);
    }
}