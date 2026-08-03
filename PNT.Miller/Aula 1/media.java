public class Media {   
    public static void main(String[] args) {
        int[] numeros = {10, 20, 30, 40, 50};
        double media = calcularMedia(numeros);
        System.out.println("A média é: " + media);
    }

    public static double calcularMedia(int[] numeros) {
        int soma = 0;
        for (int numero : numeros) {
            soma += numero;
        }
        return (double) soma / numeros.length;
    }
}