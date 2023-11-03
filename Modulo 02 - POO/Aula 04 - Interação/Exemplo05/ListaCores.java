package Exemplo05;

import java.util.ArrayList;

public class ListaCores {
    public static void main(String[] args){
    int i;
    //Declara e instancia o ArrayList cores
    ArrayList<String> cores = new ArrayList<String>();
    cores.add("Azul"); //Inclui elemento no ArrayList
    cores.add("Verde");
    cores.add("Vermelho");
    cores.add("Amarelo");

    //Loop para percorrer a lista
    for (i = 0; i<cores.size();i++)
        System.out.println((i+1) + "º) "+ cores.get(i));

    //Altera elemento da lista
    cores.set(1, "Pink");//altera o elemento na posição 1 para pink
    
    i = 0;
    System.out.println("----");
    //Loop for-each para percorrer a lista
    for(String c : cores){
        System.out.println((i+1) + "º) " + c);
        i++;
    }

    //Remove elemento da lista dda posição 3: "Amarelo"
    cores.remove(3);

    i = 0;
    System.out.println("----");
    //Loop for-each para percorrer a lista
    for (String c : cores) { // imprime elemento por elemento
        System.out.println((i + 1) + "º) " + c);
        i++;
    }
    
    //Limpa a lista: exclui todos os objetos de String
    cores.clear();

    System.out.println("----");
    System.out.println("Tamanho da lista = "+cores.size());


    }
}
