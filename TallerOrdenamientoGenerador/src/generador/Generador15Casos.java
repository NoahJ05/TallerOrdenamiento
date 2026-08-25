package generador;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

public class Generador15Casos {

    public static void main(String[] args) {
        int[] tamanos = {3000, 30000, 300000, 3000000, 30000000};
        Random random = new Random(20260824L); // Semilla fija reproducible

        // Carpeta donde se guardarán los 15 archivos
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