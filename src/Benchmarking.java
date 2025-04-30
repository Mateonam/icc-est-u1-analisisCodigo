import java.util.Random;
public class Benchmarking {
    private MetodosOrdenamiento mOrdenamiento;
    
    public Benchmarking() {

        long currentMillis = System.currentTimeMillis();  //
        long currentNano = System.nanoTime();

        System.out.println(currentMillis);
        System.out.println(currentNano);

        mOrdenamiento = new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);
        Runnable tarea = ()-> mOrdenamiento.burbujaTradicional(arreglo);
        double tiempoDuracionMillis = medirCurrentTimeMilis(tarea);
        double tiempoDuracionNano = medirConNanoTime(tarea);

        System.out.println("Tiempo en milisegundos: " + tiempoDuracionMillis);
        System.out.println("Tiempo en nanosegundos: " + tiempoDuracionNano);


    }

    private int[] generarArregloAleatorio(int tamanio) {
        int[] array = new int[tamanio];
        Random random = new Random();
        for (int i = 0; i < tamanio; i++){
            array[i] = random.nextInt(10000000);
        }
        return array;
    }

    public double medirCurrentTimeMilis(Runnable tarea) {
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos = (fin - inicio) / 1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea) {
        long inicio = System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000_000.0;
    }
}
