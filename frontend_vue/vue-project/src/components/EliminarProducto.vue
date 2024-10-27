<template>
    <div class="container mt-5">
      <h2>Eliminar Producto</h2>
  
      <div class="mb-3">
        <label for="id" class="form-label">ID del producto</label>
        <input type="number" class="form-control" id="id" v-model="id" required />
      </div>
  
      <button @click="eliminarProducto" class="btn btn-danger">Eliminar Producto</button>

      <router-link to="/" class="btn btn-secondary mt-3">Volver</router-link>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import axios from 'axios';
    
    const id = ref(0);
    
    const eliminarProducto = async () => {
        try {
            // Verificamos que el ID sea válido
            if (id.value <= 0) {
                alert('Por favor, ingrese un ID de producto válido.');
                return;
            }
        
            // Realizamos la solicitud DELETE a la API
            await axios.delete(`http://127.0.0.1:3000/productos/${id.value}`);
            alert('Producto eliminado exitosamente.');
        } catch (error) {
            alert('Error al eliminar el producto.');
            console.error(error);
        }
    };

</script>
