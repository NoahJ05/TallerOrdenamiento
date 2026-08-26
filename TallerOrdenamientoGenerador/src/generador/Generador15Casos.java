package generador;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

/**
 * Clase encargada de generar los conjuntos de datos de prueba para evaluar 
 * los algoritmos de ordenamiento.
 * 
 * Genera 15 archivos de texto plano (.txt) correspondientes a 5 tamaños 
 * de datos (3.000, 30.000, 300.000, 3.000.000, 30.000.000) divididos en 
 * 3 casos (Mejor, Peor, Promedio).
 * 
 * @author Johan Mauricio Orozco Garcia
 * @version 1.0
 */
public class Generador15Casos {

    /**
     * Metodo principal que ejecuta la generacion de los arreglos.
     * Utiliza una semilla fija para garantizar la reproducibilidad de los datos.
     * 
     * @param args Argumentos de linea de comandos (no utilizados).
     */
    public static void main(String[] args) {
        int[] tamanos = {3000, 30000, 300000, 3000000, 30000000};
        Random random = new Random(20260824L); // Semilla fija reproducible

        File carpeta = new File("datos_pruebas");
        if (!carpeta.exists()) {
            carpeta.mkdirs();
        }

        for (int tamano : tamanos) {
            System.out.println("Generando casos para N = " + tamano + "...");

            // 1. Caso Promedio (Aleatorio)
            int[] promedio = new int[tamano];
            for (int i = 0; i < tamano; i++) {
                promedio[i] = random.nextInt(Integer.MAX_VALUE);
            }
            guardarArchivo("datos_pruebas/arreglo_" + tamano + "_promedio.txt", promedio);

            // 2. Peor Caso (Orden Ascendente / Inverso para orden descendente)
            int[] peor = Arrays.copyOf(promedio, promedio.length);
            Arrays.sort(peor);
            guardarArchivo("datos_pruebas/arreglo_" + tamano + "_peor.txt", peor);

            // 3. Mejor Caso (Ya ordenado Descendente)
            int[] mejor = new int[tamano];
            for (int i = 0; i < tamano; i++) {
                mejor[i] = peor[tamano - 1 - i];
            }
            guardarArchivo("datos_pruebas/arreglo_" + tamano + "_mejor.txt", mejor);
        }

        System.out.println("\n¡Los 15 archivos fueron generados con exito en la carpeta /datos_pruebas!");
    }

    /**
     * Escribe secuencialmente un arreglo de enteros en un archivo de texto.
     * 
     * @param ruta  Directorio y nombre del archivo destino.
     * @param datos Arreglo de numeros enteros a persistir en disco.
     */
    private static void guardarArchivo(String ruta, int[] datos) {
        System.out.println("Guardando: " + ruta);
        try (BufferedWriter escritor = new BufferedWriter(new FileWriter(ruta), 64 * 1024)) {
            for (int num : datos) {
                escritor.write(Integer.toString(num));
                escritor.newLine();
            }
        } catch (IOException e) {
            System.err.println("Error al escribir " + ruta + ": " + e.getMessage());
        }
    }
}
            // 3. Mejor Caso (Ya ordenado Descendente)
            int[] mejor = new int[tamano];
            for (int i = 0; i < tamano; i++) {
                mejor[i] = peor[tamano - 1 - i];
            }
            guardarArchivo("datos_pruebas/arreglo_" + tamano + "_mejor.txt", mejor);
        }

        System.out.println("\n¡Los 15 archivos fueron generados con éxito en la carpeta /datos_pruebas!");
    }

    private static void guardarArchivo(String ruta, int[] datos) {
        System.out.println("Guardando: " + ruta);
        try (BufferedWriter escritor = new BufferedWriter(new FileWriter(ruta), 64 * 1024)) {
            for (int num : datos) {
                escritor.write(Integer.toString(num));
                escritor.newLine();
            }
        } catch (IOException e) {
            System.err.println("Error al escribir " + ruta + ": " + e.getMessage());
        }
    }
}
