package Soma;

import java.util.Scanner;

import javax.sound.sampled.SourceDataLine;

public class OlaMundo {
    public static void main(String[] args){
        Scanner leitor = new Scanner(System.in);
        int x, y, z;//variaveis locais

        System.out.println("Olá mundo da soma!");
        System.out.print("Entre com o valor de x: ");
        x = leitor.nextInt();
        System.out.print("Entre com o valor de y: ");
        y = leitor.nextInt();
        z = x + y;
        System.out.println("A soma de x + y = "+z);
    }
}
