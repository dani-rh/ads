package Exercicio02;

public class Produto {
    private String nome;
    private double preco;
    private int quantidadeEmEstoque;

    public Produto(String nome, double preco, int quantidadeEmEstoque){
        this.nome = nome;
        this.preco = preco;
        this.quantidadeEmEstoque = quantidadeEmEstoque;
    }

    public String getNome(){
        return nome;
    }

    public double getPreco(){
        return preco;
    }

    public int getQuantidadeEmEstoque(){
        return quantidadeEmEstoque;
    }

    public void decrementarEstoque(){
        if(this.quantidadeEmEstoque > 0){
            this.quantidadeEmEstoque -=1 ;
        }else{
            System.out.println("Estoque esgotado para o produto: "+this.nome);
        }
    }
}
