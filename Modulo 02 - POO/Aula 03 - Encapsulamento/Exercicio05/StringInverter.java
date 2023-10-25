package Exercicio05;
/*Crie um método que receba uma string e retorne essa mesma string, mas ao contrário. Por exemplo: ao informar a string “Valorant” o método deve retornar “tnarolaV”.
 */
public class StringInverter {
    public static String invertString(String original) {
        String invertida = "";
        for(int i = original.length() - 1; i >= 0; i--) {
            invertida = invertida + original.charAt(i);
        }
        return invertida;
    }

    public static void main(String[] args) {
        String original = "Valorant";
        String invertida = invertString(original);
        System.out.println("String original: " + original);
        System.out.println("String invertida: " + invertida);
    }
}
