public class Lampada {
    private boolean acesa; //atributo

    public void acender(){ //método publico
        this.acesa = true;
    }

    public void apagar(){ //método publico
        this.acesa = false;
    }

    public Lampada(boolean acesa){//método construtor da classe
        this.acesa = acesa;
    }

    public boolean isAcessa(){//"getter" é is para boolean
        return this.acesa;
    }

    public void setAcesa(boolean acesa){//setter
        this.acesa = acesa;
    }

    public static void main(String[] args) {
        int cont = 1; //variavel local
        Lampada lamp1 = new Lampada(true);//instanciando objeto
        Lampada lamp2 = new Lampada(false);//instanciando objeto

        while (cont < 5){
            System.out.println("-- Iteração (repetição): " + cont);
            System.out.println("Lampada [lamp1] = " + (lamp1.isAcessa()?"acesa":"apagada"));
            System.out.println("Lampada [lamp2] = " + (lamp2.isAcessa()?"acesa":"apagada"));
            System.out.println();
            lamp1.setAcesa(!(lamp1.isAcessa()));//troca o estado de lamp1
            lamp2.setAcesa(!(lamp2.isAcessa()));//troca o estado de lamp2
            cont++;//aumenta cont em 1
        }


    }
}
