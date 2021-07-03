import java.util.Scanner;

/* 
    Desenvolvido por Juliane Souza
    02.07.2021

*/

public class calculadora{

    public static final int VIEW_POR_REAL = 30;
    public static final int CLIQUE_POR_VIEW = 12;
    public static final int SHARE_POR_CLIQUE = 3;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);     
        
        System.out.println("---------------------------DIVULGA TUDO---------------------------");
        System.out.print("Por favor, digite o valor inicial do seu investimento\ne lhe daremos quantas views, aproximadamente, seu anuncio vai alcancar: ");
        float valor_investido = Float.parseFloat(scanner.next()); 
        int valor_investido_inteiro = (int) valor_investido; 
        int views = valor_investido_inteiro * VIEW_POR_REAL;

        int cont = 0; //contador de compartilhamentos
        int novas_views = 0; //as views geradas por compartilhamento

        int qtd_cliques = (int) views/100 * CLIQUE_POR_VIEW; 
        int qtd_compartilhamento = (int) qtd_cliques/20 * SHARE_POR_CLIQUE; 
        novas_views = (int) 40 * qtd_compartilhamento; 
        views += novas_views;

        while(cont < 3){ //o maximo de compartilhamento em sequencia e 4

            qtd_cliques = (int) novas_views/100 * CLIQUE_POR_VIEW; 
            qtd_compartilhamento = (int) qtd_cliques/20 * SHARE_POR_CLIQUE; 
            novas_views = (int) 40 * qtd_compartilhamento; 
            cont++; 
            views += novas_views; 

        }
        
        System.out.println();
        System.out.printf("Aproximadamente %d views", views);
        System.out.println();

        scanner.close(); 
    }
}
