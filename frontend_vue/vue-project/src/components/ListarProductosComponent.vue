<template>
    <div class="container mt-5">
      <h2>Listado de Productos</h2>
      <table class="table table-striped mt-4">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Categoría</th>
            <th>Cantidad</th>
            <th>Fecha de Adquisición</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="producto in productos" :key="producto.id">
            <td>{{ producto.nombre }}</td>
            <td>{{ producto.categoria }}</td>
            <td>{{ producto.cantidad }}</td>
            <td>{{ producto.fecha_adquisicion }}</td>
          </tr>
        </tbody>
      </table>
      <router-link to="/" class="btn btn-secondary mt-3">Volver</router-link>
    </div>
   </template>
   
   <script setup>
   import { ref, onMounted } from 'vue';
   import axios from 'axios';
   
   const productos = ref([]);
   
   // Obtener los productos desde la API cuando se carga el componente
   onMounted(async () => {
    try {
      const respuesta = await axios.get('http://127.0.0.1:3000/productos');
      productos.value = respuesta.data;
    } catch (error) {
      console.error('Error al obtener los productos:', error);
    }
   });
   </script>
   
   <style scoped></style>