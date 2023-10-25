package Exercicio03;
/*Crie um método que receba uma string e retorne a mesma string, mas com a primeira letra de cada palavra em maiúsculo (como um título de filme). Exemplo: ao informar a string “o senhor dos anéis” o método deve retornar “O Senhor Dos Anéis”.
 */
public class StringUtils {
    public static String toTitleCase(String input){
        StringBuilder titleCase = new StringBuilder();
        boolean nextTitleCase = true;
        
        for(char c: input.toCharArray()){
            if(Character.isSpaceChar(c)){
                nextTitleCase = true;
            }else if(nextTitleCase){
                c = Character.toTitleCase(c);
                nextTitleCase = false;
            }
            titleCase.append(c);
        }
        return titleCase.toString();
    }
    public static void main(String[] args){
        String MyString = "o senhor dos anéis";
        String result = StringUtils.toTitleCase(MyString);
        System.out.println(result);//imprime o resultado 
    }
}
