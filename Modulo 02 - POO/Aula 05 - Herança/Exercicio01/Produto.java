package Exercicio01;

public class Produto {
    private String idProduto;
    private String nome;
    private double preco;

    public Produto(String idProduto, String nome, double preco){
        this.idProduto = idProduto;
        this.nome = nome;
        this.preco = preco;
    }

    public String getIdProduto(){
        return idProduto;
    }

    public String getNome(){
        return nome;
    }

    public double getPreco(){
        return preco;
    }
}

