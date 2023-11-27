package util;
import java.util.InputMismatchException;
import java.util.Scanner;

public class InterfaceUsuario {
    private Scanner scanner;

    public InterfaceUsuario() {
        scanner = new Scanner(System.in);
    }

    public double pedirValorImovel() {
        double valorImovel = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.println("Digite o valor do imóvel: ");
            try {
                valorImovel = scanner.nextDouble();
                if (valorImovel <= 0) {
                    System.out.println("Valor do imóvel deve ser positivo. Tente novamente:");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número válido para o valor do imóvel.");
                scanner.next();
            }
        }
        return valorImovel;
    }

    public int pedirPrazoFinanciamento() {
        int prazoFinanciamento = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.println("Digite o prazo do financiamento em anos: ");
            try {
                prazoFinanciamento = scanner.nextInt();
                if (prazoFinanciamento <= 0) {
                    System.out.println("Prazo do financiamento deve ser positivo. Tente novamente: ");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número inteiro válido para o prazo do financiamento.");
                scanner.next();
            }
        }
        return prazoFinanciamento;
    }

    public double pedirTaxaDeJuros() {
        double taxaJurosAnual = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.println("Digite a taxa de juros anual (%): ");
            try {
                taxaJurosAnual = scanner.nextDouble();
                if (taxaJurosAnual <= 0) {
                    System.out.println("Taxa de juros anual deve ser positiva. Tente novamente: ");
                } else if (taxaJurosAnual > 1000) { // Verificar taxa de juros abusiva
                    System.out.println("Taxa de juros anual não pode ser superior a 1000%. Tente novamente:");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número válido para a taxa de juros anual.");
                scanner.next(); // Evita um loop infinito
            }
        }
        return taxaJurosAnual / 100; // Converte para decimal
    }
    
    public double pedirAreaConstruida() {
        double areaConstruida = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.print("Informe a área construída da casa (em metros quadrados): ");
            try {
                areaConstruida = scanner.nextDouble();
                if (areaConstruida <= 0) {
                    System.out.println("A área construída deve ser um valor positivo. Tente novamente.");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número válido para a área construída.");
                scanner.next();
            }
        }
        return areaConstruida;
    }

    public double pedirTamanhoTerreno() {
        double tamanhoTerreno = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.print("Informe o tamanho do terreno (em metros quadrados): ");
            try {
                tamanhoTerreno = scanner.nextDouble();
                if (tamanhoTerreno <= 0) {
                    System.out.println("O tamanho do terreno deve ser um valor positivo. Tente novamente.");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número válido para o tamanho do terreno.");
                scanner.next();
            }
        }
        return tamanhoTerreno;
    }

    public int pedirNumeroVagasGaragem() {
        int numeroVagasGaragem = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.print("Informe o número de vagas de garagem do apartamento: ");
            try {
                numeroVagasGaragem = scanner.nextInt();
                if (numeroVagasGaragem < 0) {
                    System.out.println("O número de vagas de garagem deve ser um valor não negativo. Tente novamente.");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número inteiro válido para o número de vagas de garagem.");
                scanner.next();
            }
        }
        return numeroVagasGaragem;
    }

    public int pedirNumeroAndar() {
        int numeroAndar = 0;
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.print("Informe o número do andar do apartamento: ");
            try {
                numeroAndar = scanner.nextInt();
                if (numeroAndar < 0) {
                    System.out.println("O número do andar deve ser um valor não negativo. Tente novamente.");
                } else {
                    inputIsValid = true;
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Por favor, digite um número inteiro válido para o número do andar.");
                scanner.next();
            }
        }
        return numeroAndar;
    }

    public String pedirTipoZona() {
        String tipoZona = "";
        boolean inputIsValid = false;
        while (!inputIsValid) {
            System.out.print("Informe o tipo de zona do terreno (residencial/comercial): ");
            tipoZona = scanner.next();
            if (tipoZona.equalsIgnoreCase("residencial") || tipoZona.equalsIgnoreCase("comercial")) {
                inputIsValid = true;
            } else {
                System.out.println("Entrada inválida. Por favor, digite 'residencial' ou 'comercial'.");
            }
        }
        return tipoZona;
    }

    public void closeScanner() {
        if (scanner != null) {
            scanner.close();
            scanner = null;
        }
    }
}
