
public class Main {
    public static void main(String[] args) {
        String[] estudantes = new String[]{"Maria", "Pedro", "João"};

        System.out.println("Exemplo com loop for:");
        for (int i = 0; i < estudantes.length;i++){
            System.out.println("Estudante: "+estudantes[i]);
        }

        System.out.println("\n\nExemplo com loop foreach:");
        for(String estudante : estudantes){
            System.out.println("Estudante: "+estudante);
        }
    }
}