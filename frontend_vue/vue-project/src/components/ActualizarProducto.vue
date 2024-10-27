<template>
    <div class="container mt-5">
      <h2>Actualizar Producto</h2>
      <form @submit.prevent="actualizarProducto" class="mt-4">
        <div class="mb-3">
          <label for="id" class="form-label">ID</label>
          <input type="number" class="form-control" id="id" v-model="id" required />
        </div>
        <div class="mb-3">
          <label for="nombre" class="form-label">Nombre</label>
          <input type="text" class="form-control" id="nombre" v-model="nombre" required />
        </div>
        <div class="mb-3">
          <label for="categoria" class="form-label">Categoría</label>
          <input type="text" class="form-control" id="categoria" v-model="categoria" required />
        </div>
        <div class="mb-3">
          <label for="cantidad" class="form-label">Cantidad</label>
          <input type="number" class="form-control" id="cantidad" v-model="cantidad" required />
        </div>
        <div class="mb-3">
          <label for="fecha" class="form-label">Fecha de Adquisición</label>
          <input type="date" class="form-control" id="fecha" v-model="fecha" required />
        </div>
        <button type="submit" class="btn btn-success">Actualizar Producto</button>
        <router-link to="/" class="btn btn-secondary mx-2">Volver</router-link>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  // Variables reactivas para el formulario
  const id = ref(0);
  const nombre = ref('');
  const categoria = ref('');
  const cantidad = ref(0);
  const fecha = ref('');
  
  // Función para actualizar el producto
  const actualizarProducto = async () => {
    const productoActualizado = {
      nombre: nombre.value,
      categoria: categoria.value,
      cantidad: cantidad.value,
      fecha_adquisicion: fecha.value,
    };
  
    try {
      // Usamos comillas invertidas y pasamos `productoActualizado` en el cuerpo de la solicitud
      await axios.put(`http://127.0.0.1:3000/productos/${id.value}`, productoActualizado);
      alert('Producto actualizado exitosamente');
  
      // Limpiar el formulario
      nombre.value = '';
      categoria.value = '';
      cantidad.value = 0;
      fecha.value = '';
    } catch (error) {
      console.error('Error al actualizar el producto:', error);
      alert('Error al actualizar el producto');
    }
  };
  </script>