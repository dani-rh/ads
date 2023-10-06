/*11. Crie um algoritmo em Java que calcule a distância de Levenshtein entre duas Strings. A distância de Levenshtein é a quantidade mínima de edições de um único caractere (inserções, exclusões ou substituições) necessárias para mudar uma palavra para outra.
*/
public class Main {
    public static void main(String[] args) {
        String palavra1 = "banana";
        String palavra2 = "bandana";

        int distancia = calcularDistanciaLevenshtein(palavra1, palavra2);
        System.out.println("Distância de Levenshtein entre \"" + palavra1 + "\" e \"" + palavra2 + "\": " + distancia);
    }

    public static int calcularDistanciaLevenshtein(String palavra1, String palavra2) {
        int m = palavra1.length();
        int n = palavra2.length();

        int[][] matrizDistancia = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            matrizDistancia[i][0] = i;
        }

        for (int j = 0; j <= n; j++) {
            matrizDistancia[0][j] = j;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (palavra1.charAt(i - 1) == palavra2.charAt(j - 1)) {
                    matrizDistancia[i][j] = matrizDistancia[i - 1][j - 1];
                } else {
                    int deletar = matrizDistancia[i - 1][j] + 1;
                    int inserir = matrizDistancia[i][j - 1] + 1;
                    int substituir = matrizDistancia[i - 1][j - 1] + 1;

                    matrizDistancia[i][j] = Math.min(Math.min(deletar, inserir), substituir);
                }
            }
        }

        return matrizDistancia[m][n];
    }
}