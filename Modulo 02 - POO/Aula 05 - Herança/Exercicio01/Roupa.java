package Exercicio01;

public class Roupa extends Produto {
    private String tamanho;
     private String cor;
 
     public Roupa(String idProduto, String nome, double preco, String tamanho, String cor) {
         super(idProduto, nome, preco);
         this.tamanho = tamanho;
         this.cor = cor;
     }
 
     public String getTamanho() {
         return tamanho;
     }
 
     public String getCor() {
         return cor;
     }
}
